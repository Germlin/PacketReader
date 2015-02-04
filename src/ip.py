# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

import struct

class IP:
    def __init__(self,eth):
        self.__data=eth.getData()
        #item=struct.unpack('',self.__data[])
        #self.dst=self.__data[].encode('hex')
        #self.src=self.__data[].encode('hex')

    def getDst(self):
        pass

    def getSrc(self):
        pass

    def getProtocol(self):
        pass

    def isTCP(self):
        pass

    def getData(self):
        pass