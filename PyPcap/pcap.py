# -*- encoding=utf-8 -*-

import os
import collections
import base64
import struct
from packet import BasicPacket


class PcapHeader(BasicPacket):
    _pcap_header_ = (
        ('Magic', "4I", 4),
        ('minor', "2I", 2),
        ("major", "2I", 2),
        ('ThisZone', '4I', 4)

    )

    def __init__(self, pcap_file):
        pcap_file.seek(0, 0)
        self.field['Magic'] = pcap_file.read(4)
        self.field['Major'] = pcap_file.read(2)
        self.field['Minor'] = pcap_file.read(2)
        self.field['ThisZone'] = pcap_file.read(4)
        self.field['SigFigs'] = pcap_file.read(4)
        self.field['SanpLen'] = pcap_file.read(4)
        self.field['LinkType'] = pcap_file.read(4)

    def __str__(self):
        string = ''
        for key in self.field:
            string = string + key.ljust(16) + str(base64.b16encode(self.field[key]))[2:-1] + '\n'
        return string


class PacketHeader:
    def __init__(self, pcap_file, whence):
        self.field = collections.OrderedDict()
        self.fieldItem = ['TimestampSec', 'TimestampMSe', 'Caplen', 'Length']
        pcap_file.seek(whence, 0)
        field_data = struct.unpack('4I', pcap_file.read(16))
        index = 0
        for key in self.fieldItem:
            self.field[key] = field_data[index]
            index += 1

    def get_packet_length(self):
        return self.field['Caplen']

    def __str__(self):
        temp_str = ''
        for key in self.field:
            temp_str = temp_str + key.ljust(16) + str(self.field[key]) + '\n'
        return temp_str


class Pcap(BasicPacket):

    _pcap_header_structure = (
        ('Magic', 'I', 4),
        ('Minor', 'H', 2),
        ('Major', 'H', 2),
        ('ThisZone', 'I', 4),
        ('SignFigs', 'I', 4),
        ('SanpLen', 'I', 4),
        ('LinkType', 'I', 4),
    )

    def __init__(self, file_name):
        super(Pcap,self).__init__(self._pcap_header_)
        self._pcap_file_ = open(file_name, 'rb')
        self._pcap_header_ = self.parse(self._pcap_file_.read(self._header_length_))
        self._packet_ = self._get_packet_()
        self._pcap_length_ = int(os.path.getsize(file_name))

    def pcap_header(self):
        return self._pcap_header_

    def __del__(self):
        self._pcap_file_.close()

    def _get_packet_(self):
        res = list()
        whence = 24
        index = 0
        while whence < self._pcap_length_:
            header = PacketHeader(self.__pcapFile, whence)
            data_length = header.get_packet_length()
            data = self.__pcapFile.read(data_length)
            packet = Packet(header, data, index)
            res.append(packet)
            whence = whence + data_length + 16
            index += 1
        return res

    def packet_num(self):
        return len(self.__packet)

    def get_packet(self):
        return self.__packet


class Packet:
    def __init__(self, packet_header, packet_data, index):
        self.__packetHeader = packet_header
        self.__packetData = packet_data
        self.index = index

    def get_data(self):
        return self.__packetData

    def get_header(self):
        return self.__packetHeader
