# -*- encoding=utf-8 -*-

import struct

PCAP_HEADER = (
    ('MAG', 'I'),  # magic number
    ('MAJ', 'H'),  # majic number
    ('MIN', 'H'),  # minor number
    ('TIZ', 'I'),  # time zone
    ('SIG', 'I'),  # timestamp
    ('LEN', 'I'),  # snapshot length
    ('LTY', 'I'),  # type of link-layer
)

PACKET_HEADER = (
    ('TSS', 'I'),  # timestamp in second
    ('TSM', 'I'),  # timestamp in microsecond
    ('CLEN', 'I'),  # length of packet data that should be captured
    ('LEN', 'I'),  # the actual length of the packet
)

ETHERNET_HEADER = (
    ('DST', '6s'),  # destination MAC address
    ('SRC', '6s'),  # source MAC addr
    ('PTO', 'H'),  # protocol of network-layer
)

IP_HEADER = (
    ('VL', 'B'),  # version and length of header
    ('TOS', 'B'),  # type of services
    ('LEN', 'H'),  # length of the packet
    ('ID', 'H'),  # identification of the packet
    ('OFF', 'H'),  # offset of the segment
    ('TTL', 'B'),  # time to live
    ('PTO', 'B'),  # protocol of transport layer
    ('CKS', 'H'),  # checksum
    ('SRC', '4s'),  # source IP address
    ('DST', '4s'),  # destination IP address
)

TCP_HEADER = (
    ('SRC', 'H'),  # source port
    ('DST', 'H'),  # destination port
    ('SEQ', 'I'),  # sequence number
    ('ACK', 'I'),  # acknowledgment number
    ('LEN', 'B'),  # data offset
    ('FLG', 'B'),  # flags
    ('WIN', 'H'),  # window size
    ('CKS', 'H'),  # checksum
    ('URP', 'H'),  # urgent pointer
)

UDP_HEADER = (
    ('SRC', 'H'),  # source port
    ('DST', 'H'),  # destination port
    ('LEN', 'H'),  # length of packet
    ('CKS', 'H'),  # checksum
)


class Packet:
    """
    Packet provide functions to parse ip packets or tcp packets.
    """
    def __init__(self):
        self.ip_header = None
        self.tcp_header = None
        self.udp_header = None

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

    @staticmethod
    def ip_address(ip):
        return '.'.join(["%d" % x for x in ip])

    @staticmethod
    def mac_address(mac):
        return ':'.join(["%02X" % x for x in mac])

    @property
    def quintuple(self):
        if self.ip_header is None:
            raise ArithmeticError()
        
        src_ip = self.ip_address_format(self.ip_header['SRC'])
        dst_ip = self.ip_address_format(self.ip_header['DST'])
        if self.tcp_header is not None:
            src_port = self.tcp_header['SRC']
            dst_port = self.tcp_header['DST']
        elif self.udp_header is not None:
            src_port = self.udp_header['SRC']
            dst_port = self.udp_header['DST']
        protocol = self.ip_header['PTO']
        return src_ip, src_port, dst_ip, dst_port, protocol

    def __repr__(self):
        return "Packet %d Information: \n" % (self.id)  \
            + "[1] Epoch Time: %d.%d seconds\n" % (self.packet_header['TSS'], self.packet_header['TSM']) \
            + "[2] Frame Length: %d bytes\n" % (self.packet_header['LEN']) \
            + "[3] Destination Mac Address: %s\n" % (self.mac_address_format(self.ethernet_header['DST'])) \
            + "[4] Source Mac Address: %s\n" % (self.mac_address_format(self.ethernet_header['SRC'])) \
            + "[5] Destination IP Address: %s\n" % (self.ip_address_format(self.ip_header['DST'])) \
            + "[6] Source IP Address: %s\n" % (self.ip_address_format(self.ip_header['SRC'])) \
            + "[7] Destination Port: %s\n" % (self.tcp_header['DST']) \
            + "[8] Source Port :%s\n" % (self.tcp_header['SRC']) \
            + "[9] Protocol: %d\n" % (self.ip_header['PTO'])


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
