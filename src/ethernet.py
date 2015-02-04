# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

class ethernet:
    def __init__(self,packet):
        self.__data=packet.getData()
        self.dst=self.__data[0:6].encode('hex')
        self.src=self.__data[6:12].encode('hex')
        self.type=self.__data[12:14].encode('hex')

    def getDst(self):
        s=list()
        for i in range(6) :
            s.append( self.dst[i*2:i*2+2] )
        return ":".join(s)

    def getSrc(self):
        s=list()
        for i in range(6) :
            s.append( self.src[i*2:i*2+2] )
        return ":".join(s)

    def getType(self):
        return self.type

    def isIP(self):
        return self.type=='0800'

    def getData(self):
        return self.__data[14:]