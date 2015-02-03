# -*- encoding=cp936 -*-

import os
import sys
import types
import collections
import struct


class PcapHeader:
    '''
    This is the header of Pcap file.
    '''
    __field = collections.OrderedDict()

    def __init__(self, pcapFile):
        if (type(pcapFile) == types.FileType):
            if (not pcapFile.closed):
                pcapFile.seek(0, 0)
                self.__field['Magic'] = pcapFile.read(4).encode('hex')
                self.__field['Major'] = pcapFile.read(2).encode('hex')
                self.__field['Minor'] = pcapFile.read(2).encode('hex')
                self.__field['ThisZone'] = pcapFile.read(4).encode('hex')
                self.__field['SigFigs'] = pcapFile.read(4).encode('hex')
                self.__field['SanpLen'] = pcapFile.read(4).encode('hex')
                self.__field['LinkType'] = pcapFile.read(4).encode('hex')
        else:
            print "Can not open the pcapFile."

    def __str__(self):
        str = ''
        for key in self.__field:
            str = str + key.ljust(16) + self.__field[key] + '\n'
        return str


class PacketHeader:
    '''
    This is the header of Packet
    '''
    __field = collections.OrderedDict()

    def __init__(self, pcapFile, whence):
        self.__fieldItem = ['TimestampSec', 'TimestampMSe', 'Caplen', 'Length']
        if (type(pcapFile) == types.FileType):
            if (not pcapFile.closed):
                pcapFile.seek(whence, 0)
                fieldData = struct.unpack('4I', pcapFile.read(16))
                index = 0
                for key in self.__fieldItem:
                    self.__field[key] = fieldData[index]
                    index = index + 1
        else:
            print "Can not open the pcapFile."

    def getPacketLength(self):
        return self.__field['Caplen']

    def __str__(self):
        tempStr = ''
        for key in self.__field:
            tempStr = tempStr + key.ljust(16) + str(self.__field[key]) + '\n'
        return tempStr


class PcapFile:
    def __init__(self, fileName):
        self.__pcapLength = int(os.path.getsize(fileName))
        self.__pcapFile = open(fileName, 'rb')
        self.__pcapHeader = PcapHeader(self.__pcapFile)
        self.getPacketHeader()

    def __len__(self):
        return self.__pcapLength

    def getPcapHeader(self):
        return self.__pcapHeader

    def __del__(self):
        self.__pcapFile.close()

    def getPacketHeader(self):
        self.__packetHeader = []
        whence = 24
        while whence < self.__pcapLength:
            x = PacketHeader(self.__pcapFile, whence)
            whence = whence + x.getPacketLength() + 16
            self.__packetHeader.append(x)

    def getPacketHeaderNum(self):
        return len(self.__packetHeader)

    def getPacketData(self):
        pass

    def followTCPstream(self, ip):
        pass

        