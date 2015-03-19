# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'

from utility import *

class PcapHeader:
    def __init__(self, pcapFile):
        self.field = collections.OrderedDict()
        pcapFile.seek(0, 0)
        self.field['Magic'] = pcapFile.read(4)
        self.field['Major'] = pcapFile.read(2)
        self.field['Minor'] = pcapFile.read(2)
        self.field['ThisZone'] = pcapFile.read(4)
        self.field['SigFigs'] = pcapFile.read(4)
        self.field['SanpLen'] = pcapFile.read(4)
        self.field['LinkType'] = pcapFile.read(4)

    def __str__(self):
        string = ''
        for key in self.field:
            string = string + key.ljust(16) + str(base64.b16encode(self.field[key]))[2:-1] + '\n'
        return string


class PacketHeader:
    def __init__(self, pcapFile, whence):
        self.field = collections.OrderedDict()
        self.fieldItem = ['TimestampSec', 'TimestampMSe', 'Caplen', 'Length']
        pcapFile.seek(whence, 0)
        fieldData = struct.unpack('4I', pcapFile.read(16))
        index = 0
        for key in self.fieldItem:
            self.field[key] = fieldData[index]
            index = index + 1

    def getPacketLength(self):
        return self.field['Caplen']

    def __str__(self):
        tempStr = ''
        for key in self.field:
            tempStr = tempStr + key.ljust(16) + str(self.field[key]) + '\n'
        return tempStr


class PcapFile:
    def __init__(self, fileName):
        self.__pcapLength = int(os.path.getsize(fileName))
        self.__pcapFile = open(fileName, 'rb')
        self.__pcapHeader = PcapHeader(self.__pcapFile)
        self.__packet = self._getPacket()

    def __len__(self):
        return self.__pcapLength

    def getPcapHeader(self):
        return self.__pcapHeader

    def __del__(self):
        self.__pcapFile.close()

    def _getPacket(self):
        res = list()
        whence = 24
        index = 0
        while whence < self.__pcapLength:
            header = PacketHeader(self.__pcapFile, whence)
            dataLength = header.getPacketLength()
            data = self.__pcapFile.read(dataLength)
            packet = Packet(header, data, index)
            res.append(packet)
            whence = whence + dataLength + 16
            index = index + 1
        return res

    def packetNum(self):
        return len(self.__packet)

    def getPacket(self):
        return self.__packet


class Packet:
    def __init__(self, packet_header, packet_data, index):
        self.__packetHeader = packet_header
        self.__packetData = packet_data
        self.index = index

    def getData(self):
        return self.__packetData

    def getHeader(self):
        return self.__packetHeader
