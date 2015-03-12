__author__ = 'Reuynil'

from input import *
from utility import *
from ip import *


class TcpDatagram:
    def __init__(self, dst_stocket, src_stocket):
        pass

class TCP:
    def __init__(self, ip_datagram):
        self.__data = ip_datagram.data
        self.fields = collections.OrderedDict()
        self.items = ("SrcPort", "DstPort", "Seq", "Ack", "Length", "Flags", "Win", "Sum", "Urp")
        index = 0
        for value in struct.unpack('!2H2L2B3H', self.__data[:20]):
            self.fields[self.items[index]] = value
            index += 1

    # TODO:
    def check_sum(self):
        pass

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
        return testBit(self.fields["Flags"], 1)

    def test_ack(self):
        return testBit(self.fields["Flags"], 4)

    def test_fin(self):
        return testBit(self.fields["Flags"], 0)

    @staticmethod
    def reassemble_tcp(pcap):
        assert isinstance(pcap, PcapFile)
        ip_packet = reassembleIP(pcap)
        work_list = dict()
        for pk in ip_packet:
            assert isinstance(pk, ipDatagram)
            if pk.protocol == 'IP_PROTO_TCP':
                pk_dst_ip, pk_src_ip = pk.dst, pk.src
                pk_tcp = TCP(pk)
                pk_dst_port, pk_src_port = pk_tcp.get_dst_port(), pk_tcp.get_src_port()
                quadruple = (pk_dst_ip, pk_dst_port, pk_src_ip, pk_src_port)
                if quadruple in work_list.keys():
                    work_list[quadruple].append(pk_tcp)
                else:
                    work_list[quadruple] = [pk_tcp]
        for k in work_list:
            data = b''
            tcp_segment_list = work_list[k]
            tcp_segment_list.sort(key=lambda x: x.get_seq())

            # delete
            print(k)
            for kk in tcp_segment_list:
                print(kk.get_seq())
            # end of delete

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

                    # delete
                    print(seg_next, seg_begin)
                    #end of delete

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
                        seg_next = seg_next + 1
