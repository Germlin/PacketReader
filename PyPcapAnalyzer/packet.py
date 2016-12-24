# -*- encoding=utf-8 -*-

import struct


PCAP_HEADER = (
    ('MAG', 'I', 4),    # magic number
    ('MAJ', 'H', 2),    # majic number
    ('MIN', 'H', 2),    # minor number
    ('TIZ', 'I', 4),    # time zone
    ('SIG', 'I', 4),    # timestamp
    ('LEN', 'I', 4),    # snapshot length
    ('LTY', 'I', 4),    # type of link-layer
)

PACKET_HEADER = (
    ('TSS', 'I', 4),    # timestamp in second
    ('TSM', 'I', 4),    # timestamp in microsecond
    ('CLEN', 'I', 4),   # length of packet data that were caputure
    ('LEN', 'I', 4),    # the actual length of the packet
)

ETHERNET_HEADER = (
    ('DST', '6B', 6),   # destination MAC address
    ('SRC', '6B', 6),   # source MAC address
    ('PTO', 'H', 2),    # protocol of network-layer
)

IP_HEADER = (
    ('VL', 'B', 1),     # version and length of header
    ('TOS', 'B', 1),    # type of services
    ('LEN', 'H', 2),    # length of the packet
    ('ID', 'H', 2),     # identification of the packet
    ('OFF', 'H', 2),    # offset of the segment
    ('TTL', 'B', 1),    # time to live
    ('PTO', 'B', 1),    # protocol of transport layer
    ('CKS', 'H', 2),    # checksum
    ('SRC', 'I', 4),    # source IP address
    ('DST', 'I', 4),    # destination IP address
)

TCP_HEADER = (
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

    def ip_address_format(ip):
        s = []
        while ip:
            tmp = ip % 256
            s.insert(0,str(tmp))
            ip //= 256
        return str(".".join(s))

    def mac_address_format(mac):
        s = []
        for i in mac:
            s.append(hex(i)[2:])
        return str(":".join(s))


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
        if len(x[1]) == 1 or x[1][1] == 's':
            header[x[0]] = lst[index]
            index += 1
        else:
            ls_len = int(x[1][0])
            header[x[0]] = lst[index:index + ls_len]
            index += ls_len
    return header
