# -*- encoding=utf-8 -*-

from PyPcapAnalyzer.ip import *

_TCP_header_structure_ = (
    ('SRC', 'H', 2),
    ('DST', 'H', 2),
    ('SEQ', 'I', 4),
    ('ACK', 'I', 4),
    ('LEN', 'B', 1),
    ('FLG', 'B', 1),
    ('WIN', 'H', 2),
    ('CKS', 'H', 2),
    ('URP', 'H', 2),
)


class TCPPacket(BasicPacket):
    """
    理论上，传入的不应该是IPPacket，而应该是IPDatagram，但是由于TCP会尽量保证IP层不分片，所以我直接用了IPPacket。
    """
    def __init__(self, pt):
        super(TCPPacket, self).__init__(_TCP_header_structure_)
        self._parse_header_(pt.data[0:self._header_length_])
        # CHECKSUM
        pseudo_header = struct.pack('!2IBBH', pt.src_ip, pt.dst_ip,0,6,len(pt.data))
        check_data = pseudo_header + pt.data
        if len(check_data) % 2 != 0:
            check_data = check_data + b'\x00'
        self.check_sum = self.checksum(check_data)
        # END OF CHECKSUM
        if self.syn:
            self.data = b''
        else:
            self.data = pt.data[self.header_length:]
        self.data_length = len(self.data)

    @property
    def src_port(self):
        return self.header['SRC']

    @property
    def dst_port(self):
        return self.header['DST']

    @property
    def header_length(self):
        return (self.header['LEN'] >> 4) * 4

    @property
    def seq(self):
        return self.header['SEQ']

    @property
    def ack_seq(self):
        return self.header['ACK']

    @property
    def fin(self):
        mask = 0b00000001 << 0
        return (self.header['FLG'] & mask) >> 0

    @property
    def syn(self):
        mask = 0b00000001 << 1
        return (self.header['FLG'] & mask) >> 1

    @property
    def rst(self):
        mask = 0b00000001 << 2
        return (self.header['FLG'] & mask) >> 2

    @property
    def psh(self):
        mask = 0b00000001 << 3
        return (self.header['FLG'] & mask) >> 3

    @property
    def ack(self):
        mask = 0b00000001 << 4
        return (self.header['FLG'] & mask) >> 4

    @property
    def urg(self):
        mask = 0b00000001 << 5
        return (self.header['FLG'] & mask) >> 5

    @property
    def win(self):
        return self.header['WIN']


class TcpDatagram:
    def __init__(self, quadruple, tcp_data):
        self.src_socket = quadruple[0:2]
        self.dst_socket = quadruple[2:4]
        self.data = tcp_data

    def length(self):
        return len(self.data)


def tcp_reassemble(ip_packets):
    """
    输入一组IP数据包。
    :param ip_datagrams:
    :return:
    """
    work_list = dict()
    for pk in ip_packets:
        if pk.protocol == 6:
            pk_tcp = TCPPacket(pk)
            pk_dst_ip, pk_src_ip = pk.dst_ip, pk.src_ip
            pk_dst_port, pk_src_port = pk_tcp.dst_port, pk_tcp.src_port
            quadruple = (pk_dst_ip, pk_dst_port, pk_src_ip, pk_src_port)
            if quadruple in work_list.keys():
                work_list[quadruple].append(pk_tcp)
            else:
                work_list[quadruple] = [pk_tcp]

    res = list()
    for k in work_list:
        data = b''
        tcp_segment_list = work_list[k]
        tcp_segment_list.sort(key=lambda x: x.seq)
        seg_next = tcp_segment_list[0].seq
        for tcp_segment in tcp_segment_list:
            if tcp_segment.syn:
                seg_next = tcp_segment.seq + 1
            else:
                seg_begin = tcp_segment.seq
                seg_len = tcp_segment.data_length
                seg_end = seg_begin + seg_len
                seg_data = tcp_segment.data
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
                    #其实更好的方法应该是用零字节填充漏掉的内容，然后在重组完的TCP数据
                    #报上标注。

                if tcp_segment.fin:
                    seg_next += 1

                if tcp_segment.psh:
                    res.append(TcpDatagram(k, data))
                    data = b''
        res.append(TcpDatagram(k, data))
    return res
