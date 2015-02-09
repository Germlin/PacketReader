# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

# 包括IP数据报的类，同时还有一个函数，把一个已经分片的IP数据报重组



class ip:
    '''
    包括以下函数：获取源IP地址，获取目的IP地址，检验IP数据校验和。
    '''

    def __init__(self, eth):
        '''
        初始化函数。
        :param eth: 一个ethernet类对象，通过getData()函数可以获得网络层的字节流
        :return:
        '''
        self.fields = {"version": None,
                       "HeaderLength": None,
                       "DSCP": None,
                       "ECN": None,
                       "TotalLength": None,
                       "Identification": None,
                       "Flags": None,
                       "FragmentOffset": None,
                       "TTL": None,
                       "Protocol": None,
                       "Checksum": None,
                       "SourceIP": None,
                       "DestinationIP": None,
                       "Options": None}
        self.__data = eth.getData()
        self.fields["SourceIP"] = self.__data[12:16]
        self.fields["DestinationIP"] = self.__data[16:20]
        self.fields["HeaderLength"] = self.__getFiled(0, 4, 4) * 4
        self.fields["Checksum"] = self.__getFiled(10, 0, 8)

    def getDst(self):
        s = list()
        for i in range(4):
            s.append(str(int(self.fields["DestinationIP"][i:i + 1].encode('hex'), 16)))
        return ".".join(s)

    def getSrc(self):
        s = list()
        for i in range(4):
            s.append(str(int(self.fields["SourceIP"][i:i + 1].encode('hex'), 16)))
        return ".".join(s)

    def getProtocol(self):
        pass

    def isTCP(self):
        pass

    def getData(self):
        pass

    def __getFiled(self, byteOffset, bitOffset, length):
        '''
        获取header指定的数据域，比如第四个字节的后四位。
        :param header: 数据头，字节流
        :param byteOffset: 数据域开始的字节位置
        :param bitOffset: 数据域开始的位位置
        :param length: 数据域的长度，按照bit计算
        :return:int类型，不足一个字节的，在高位补0，然后再转成十进制
        '''
        byteLength = (length - (8 - bitOffset)) / 8 + 1
        data = self.__data[byteOffset:byteOffset + byteLength]
        mask = 2 ** (byteLength * 8 - bitOffset) - 1
        data_int = int(data.encode('hex'), 16)
        res = data_int & mask
        return res

    def checkSum(self):
        check_sum = 0
        i = 0
        while i < self.fields["HeaderLength"]:
            check_sum += self.__getFiled(i, 0, 16)
            i += 2
        check_sum = (check_sum >> 16) + (check_sum & 0xffff)
        return check_sum == 0xffff


def resumble(packet_list, dst, src):
    pass


