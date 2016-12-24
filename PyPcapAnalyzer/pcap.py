# -*- encoding=utf-8 -*-

from .packet import *


def read_pcap(file_name):
    packets = []
    with open(file_name,'rb') as file:
        file.seek(0, 2)
        pcap_length = file.tell()
        file.seek(0, 0)
        pcap_header = parse_header(file.read(24), PCAP_HEADER, order='S')
        whence = 24 # the first 24 byte is the header of pcap file
        while whence < pcap_length:
            file.seek(whence, 0)
            packet = Packet()
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
                    else if packet.ip_header['PTO'] == 17:
                        packet.udp_header = parse_header(file.read(), UDP_HEADER)
                    else:
                        raise PacketTypeError()
                else:
                    raise PacketTypeError()
            else:
                raise PacketTypeError()
            data_length = packet.packet_header['CLEN']
            packets.append(packet)
            whence = whence + data_length + 16
    return packets
