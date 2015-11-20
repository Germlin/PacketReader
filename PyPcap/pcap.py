# -*- encoding=utf-8 -*-

import os
from PyPcap.packet import BasicPacket


class Pcap(BasicPacket):
    _pcap_header_structure_ = (
        ('Magic', 'I', 4),
        ('Minor', 'H', 2),
        ('Major', 'H', 2),
        ('ThisZone', 'I', 4),
        ('SignFigs', 'I', 4),
        ('SanpLen', 'I', 4),
        ('LinkType', 'I', 4),
    )

    def __init__(self, file_name):
        super(Pcap, self).__init__(self._pcap_header_structure_)
        self._pcap_file_ = open(file_name, 'rb')
        self._parse_header_(self._pcap_file_.read(self._header_length_))
        self.packets = self._get_packet_()
        self.packets_num = len(self.packets)
        self._pcap_length_ = int(os.path.getsize(file_name))

    def __del__(self):
        self._pcap_file_.close()

    def _get_packet_(self):
        res = list()
        whence = 24
        index = 0
        while whence < self._pcap_length_:
            packet = Packet(self._pcap_file_.read(16), index)
            data_length = packet.packet_length()
            data = self._pcap_file_.read(data_length)
            packet.data = data
            res.append(packet)
            whence = whence + data_length + 16
            index += 1
        return res


class Packet(BasicPacket):
    _packet_header_structure_ = (
        ('TimestampSec', 'I', 4),
        ('TimestampMSe', 'I', 4),
        ('CaptureLength', 'I', 4),
        ('Length', 'I', 4),
    )

    def __init__(self, header, index):
        super(Packet, self).__init__(self._packet_header_structure_)
        self._parse_header_(header)
        self.data = b''
        self.index = index

    def packet_length(self):
        return self.header['CaptureLength']
