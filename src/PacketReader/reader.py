# -*- encoding=utf-8 -*-

from PacketReader.packet import *
from PacketReader.exception import PacketTypeError

def read_pcap(file_name):
    packets = []
    with open(file_name, 'rb') as file:
        file.seek(0, 2)
        pcap_length = file.tell()
        file.seek(0, 0)
        pcap_header = parse_header(file.read(24), PCAP_HEADER, order='S')
        whence = 24  # the first 24 byte is the header of pcap file
        id = 1
        while whence < pcap_length:
            file.seek(whence, 0)
            packet = Packet()
            packet.id = id
            id += 1
            packet.packet_header = parse_header(file.read(16), PACKET_HEADER, order='S')
            if pcap_header['LTY'] == 0x01:
                packet.ethernet_header = parse_header(file.read(14), ETHERNET_HEADER)
                if packet.ethernet_header['PTO'] == 0x0800:
                    packet.ip_header = parse_header(file.read(20), IP_HEADER)
                    packet.ip_header_format()
                    file.seek(packet.ip_header['HLEN'] - 20, 1)
                    if packet.ip_header['PTO'] == 6:
                        packet.tcp_header = parse_header(file.read(20), TCP_HEADER)
                        packet.tcp_header_format()
                    elif packet.ip_header['PTO'] == 17:
                        packet.udp_header = parse_header(file.read(8), UDP_HEADER)
                    else:
                        raise PacketTypeError("PacketReader can only parse tcp or udp packet.")
                else:
                    raise PacketTypeError("PacketReader can only parse ip packet.")
            else:
                raise PacketTypeError("PacketReader can only parse ethernet packet.")
            data_length = packet.packet_header['CLEN']
            packets.append(packet)
            whence = whence + data_length + 16
    return packets
