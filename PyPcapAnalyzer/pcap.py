# -*- encoding=utf-8 -*-

from PyPcapAnalyzer.packet import BasicPacket


class Packet(BasicPacket):
    _packet_header_structure_ = (
        ('TimestampSec', 'I', 4),
        ('TimestampMSe', 'I', 4),
        ('CaptureLength', 'I', 4),
        ('Length', 'I', 4),
    )

    def __init__(self, header, link_type):
        super(Packet, self).__init__(self._packet_header_structure_)
        self._parse_header_(header, order='S')
        self.data = b''
        self.link_type = link_type

    def packet_length(self):
        return self.header['CaptureLength']


class Pcap(BasicPacket):
    _pcap_header_structure_ = (
        ('Magic', 'I', 4),
        ('Major', 'H', 2),
        ('Minor', 'H', 2),
        ('ThisZone', 'I', 4),
        ('SignFigs', 'I', 4),
        ('SnapLen', 'I', 4),
        ('LinkType', 'I', 4),
    )

    def __init__(self, file):
        super(Pcap, self).__init__(self._pcap_header_structure_)
        self._pcap_file_ = file
        file.seek(0, 2)
        self._pcap_length_ = file.tell()
        file.seek(0, 0)
        self._parse_header_(self._pcap_file_.read(self._header_length_), order='S')
        self.packets = list()
        whence = self._header_length_
        while whence < self._pcap_length_:
            packet = Packet(self._pcap_file_.read(16), self.header['LinkType'])
            data_length = packet.packet_length()
            packet.data = self._pcap_file_.read(data_length)
            self.packets.append(packet)
            whence = whence + data_length + 16
        self.packets_num = len(self.packets)
