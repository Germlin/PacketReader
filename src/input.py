# -*- encoding=cp936 -*-

import os
import sys
import types
import collections

class PcapHeader:
    '''
    This is the header of Pcap file.
    '''
    __field=collections.OrderedDict()
    def __init__(self,pcapFile):
        if(type(pcapFile)==types.FileType):
            if(not pcapFile.closed):
                pcapFile.seek(0,0)
                self.__field['Magic'] = pcapFile.read(4).encode('hex')
                self.__field['Major']=pcapFile.read(2).encode('hex')
                self.__field['Minor']=pcapFile.read(2).encode('hex')
                self.__field['ThisZone']=pcapFile.read(4).encode('hex')
                self.__field['SigFigs']=pcapFile.read(4).encode('hex')
                self.__field['SanpLen']=pcapFile.read(4).encode('hex')
                self.__field['LinkType']=pcapFile.read(4).encode('hex')
        else:
            print "Can not open the pcapFile."
        
    def __str__(self):
        str = ''
        for key in self.__field:
            str = str+key.ljust(16)+self.__field[key]+'\n'
        return str
    
class PacketHeader:
    '''
    This is the header of Packet
    '''
    __field=collections.OrderedDict()
    def __init__(self,pcapFile,whence):
        if(type(pcapFile)==types.FileType):
            if(not pcapFile.closed):
                pcapFile.seek(whence,0)
                self.__field['TimestampHigh']=pcapFile.read(4).encode('hex')
                self.__field['TimestampLow']=pcapFile.read(4).encode('hex')
                self.__field['Caplen']=pcapFile.read(4).encode('hex')
                self.__field['Length']=pcapFile.read(4).encode('hex')
        else:
            print "Can not open the pcapFile."

    def getPacketLength(self):
        return self.__field['Caplen']

class PcapFile:
    def __init__(self,fileName):
        self.__pcapLength=os.path.getsize(fileName)
        self.__pcapFile=open(fileName,'rb')
        self.__pcapHeader=PcapHeader(self.__pcapFile)
    
    def __len__(self):
        return self.__pcapLength
    
    def getPcapHeader(self): 
        return self.__pcapHeader
    
    def __del__(self):
        self.__pcapFile.close()
        
        
        
        