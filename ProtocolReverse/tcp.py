# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import pcapreader
import utility
import ip
import os
import collections
import struct


class TcpDatagram:
    def __init__(self, quadruple, tcp_data):
        self.dst_socket = quadruple[0:2]
        self.src_socket = quadruple[2:4]
        self.data = tcp_data

    def get_data(self):
        return self.data

    def get_length(self):
        return len(self.data)

    def get_dst_socket(self):
        return ':'.join(list(map(str, self.dst_socket)))

    def get_src_socket(self):
        return ':'.join(list(map(str, self.src_socket)))

    def save(self, path):
        file_name = 'Dst_' + self.get_dst_socket().replace(':', '_') + \
                    '_Src_' + self.get_src_socket().replace(':', '_') + '.tcpd'
        file = open(os.path.join(path, file_name), 'wb')
        file.write(self.get_data())
        file.close()


class TCP:
    def __init__(self, ip_datagram):
        assert isinstance(ip_datagram, ip.IpDatagram)
        self.__data = ip_datagram.data
        self.__src = ip_datagram.src
        self.__dst = ip_datagram.dst
        self.fields = collections.OrderedDict()
        self.items = ("SrcPort", "DstPort", "Seq", "Ack", "Length", "Flags", "Win", "Sum", "Urp")
        index = 0
        for value in struct.unpack('!2H2L2B3H', self.__data[:20]):
            self.fields[self.items[index]] = value
            index += 1

    # TODO: 没有完成。
    def check_sum(self):
        source_ip = b''
        for i in self.__src.split('.'):
            source_ip += int(i).to_bytes(1, byteorder='big')
        destination_ip = b''
        for i in self.__dst.split('.'):
            destination_ip += int(i).to_bytes(1, byteorder='big')
        reserved = 0
        protocol = ip.IP_PROTO_TCP


    def get_src_port(self):
        return self.fields["SrcPort"]

    def get_dst_port(self):
        return self.fields["DstPort"]

    def get_length(self):
        return len(self.__data)

    def get_header_length(self):
        return (self.fields["Length"] >> 4) * 4

    def get_data_length(self):
        if self.test_syn():
            return 0
        else:
            return self.get_length() - self.get_header_length()

    def get_seq(self):
        return self.fields["Seq"]

    def get_ack(self):
        return self.fields["Ack"]

    def get_data(self):
        if self.test_syn():
            return b''
        else:
            return self.__data[self.get_header_length():]

    def test_syn(self):
        return utility.test_bit(self.fields["Flags"], 1)

    def test_ack(self):
        return utility.test_bit(self.fields["Flags"], 4)

    def test_fin(self):
        return utility.test_bit(self.fields["Flags"], 0)

    @staticmethod
    def reassemble_tcp(pcap):
        assert isinstance(pcap, pcapreader.PcapFile)
        ip_packet = ip.IP.reassemble_ip(pcap)
        work_list = dict()
        for pk in ip_packet:
            assert isinstance(pk, ip.IpDatagram)
            if pk.protocol == 'IP_PROTO_TCP':
                pk_dst_ip, pk_src_ip = pk.dst, pk.src
                pk_tcp = TCP(pk)
                pk_dst_port, pk_src_port = pk_tcp.get_dst_port(), pk_tcp.get_src_port()
                quadruple = (pk_dst_ip, pk_dst_port, pk_src_ip, pk_src_port)
                if quadruple in work_list.keys():
                    work_list[quadruple].append(pk_tcp)
                else:
                    work_list[quadruple] = [pk_tcp]

        res = list()
        for k in work_list:
            data = b''
            tcp_segment_list = work_list[k]
            tcp_segment_list.sort(key=lambda x: x.get_seq())
            seg_next = tcp_segment_list[0].get_seq()
            for tcp_segment in tcp_segment_list:
                assert isinstance(tcp_segment, TCP)
                if tcp_segment.test_syn():
                    seg_next = tcp_segment.get_seq() + 1
                else:
                    seg_begin = tcp_segment.get_seq()
                    seg_len = tcp_segment.get_data_length()
                    seg_end = seg_begin + seg_len
                    seg_data = tcp_segment.get_data()
                    if seg_next == seg_begin:
                        data = data + seg_data
                        seg_next = seg_end
                    elif seg_next > seg_begin:
                        if seg_next < seg_end:
                            new_data = seg_data[seg_next - seg_begin:]
                            data = data + new_data
                            seg_next = seg_end
                    else:
                        raise Exception("Lose packet.")

                    if tcp_segment.test_fin():
                        seg_next += 1
            res.append(TcpDatagram(k, data))
        return res
