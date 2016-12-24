# -*- encoding=utf-8 -*-

import struct


PCAP_HEADER = (
    ('MAG', 'I'),    # magic number
    ('MAJ', 'H'),    # majic number
    ('MIN', 'H'),    # minor number
    ('TIZ', 'I'),    # time zone
    ('SIG', 'I'),    # timestamp
    ('LEN', 'I'),    # snapshot length
    ('LTY', 'I'),    # type of link-layer
)

PACKET_HEADER = (
    ('TSS', 'I'),    # timestamp in second
    ('TSM', 'I'),    # timestamp in microsecond
    ('CLEN', 'I'),   # length of packet data that were caputure
    ('LEN', 'I'),    # the actual length of the packet
)

ETHERNET_HEADER = (
    ('DST', '6s'),   # destination MAC address
    ('SRC', '6s'),   # source MAC addr
    ('PTO', 'H'),    # protocol of network-layer
)

IP_HEADER = (
    ('VL', 'B'),     # version and length of header
    ('TOS', 'B'),    # type of services
    ('LEN', 'H'),    # length of the packet
    ('ID', 'H'),     # identification of the packet
    ('OFF', 'H'),    # offset of the segment
    ('TTL', 'B'),    # time to live
    ('PTO', 'B'),    # protocol of transport layer
    ('CKS', 'H'),    # checksum
    ('SRC', '4s'),    # source IP address
    ('DST', '4s'),    # destination IP address
)

TCP_HEADER = (
    ('SRC', 'H'),    # source port
    ('DST', 'H'),    # destination port
    ('SEQ', 'I'),    # sequence number
    ('ACK', 'I'),    # acknowledgment number
    ('LEN', 'B'),    # data offset
    ('FLG', 'B'),    # flags
    ('WIN', 'H'),    # window size
    ('CKS', 'H'),    # checksum
    ('URP', 'H'),    # urgent pointer
)


class Packet:
    def ip_header_format(self):
        if self.ip_header is None:
            raise AttributeError()
        else:
            self.ip_header['VER'] = self.ip_header['VL'] >> 4
            self.ip_header['HLEN'] = (self.ip_header['VL'] & 0x0F) * 4
            self.ip_header.pop('VL')
            self.ip_header['DF'] = self.ip_header['OFF'] & 0x4000
            self.ip_header['MF'] = self.ip_header['OFF'] & 0x2000
            self.ip_header['OFF'] = self.ip_header['OFF'] & 0x1FFF

    def tcp_header_format(self):
        if self.tcp_header is None:
            raise AttributeError()
        else:
            self.tcp_header['LEN'] = (self.tcp_header['LEN'] >> 4) * 4
            self.tcp_header['SYN'] = (self.tcp_header['FLG'] & (0b00000001 << 1)) >> 1
            self.tcp_header['RST'] = (self.tcp_header['FLG'] & (0b00000001 << 2)) >> 2
            self.tcp_header['PSH'] = (self.tcp_header['FLG'] & (0b00000001 << 3)) >> 3
            self.tcp_header['ACK'] = (self.tcp_header['FLG'] & (0b00000001 << 4)) >> 4
            self.tcp_header['URG'] = (self.tcp_header['FLG'] & (0b00000001 << 5)) >> 5
            self.tcp_header.pop('FLG')

    def ip_address_format(ip):
        return '.'.join( [ "%d" % x for x in bins ] )

    def mac_address_format(mac):
        return ':'.join( [ "%02X" % x for x in mac ] )


class PacketTypeError(Exception):
    pass


def parse_header(header_data, header_structure, order='B'):
    if order == 'B':
        fmt = '!'
    else:
        fmt = ''
    for x in header_structure:
        fmt = fmt + x[1]
    lst = struct.unpack(fmt, header_data)
    index = 0
    header = {}
    for x in header_structure:
        header[x[0]] = lst[index]
        index += 1
    return header
