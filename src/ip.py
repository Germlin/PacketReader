# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

# ����IP���ݱ����࣬ͬʱ����һ����������һ���Ѿ���Ƭ��IP���ݱ�����



class ip:
    '''
    �������º�������ȡԴIP��ַ����ȡĿ��IP��ַ������IP����У��͡�
    '''

    def __init__(self, eth):
        '''
        ��ʼ��������
        :param eth: һ��ethernet�����ͨ��getData()�������Ի���������ֽ���
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
        ��ȡheaderָ���������򣬱�����ĸ��ֽڵĺ���λ��
        :param header: ����ͷ���ֽ���
        :param byteOffset: ������ʼ���ֽ�λ��
        :param bitOffset: ������ʼ��λλ��
        :param length: ������ĳ��ȣ�����bit����
        :return:int���ͣ�����һ���ֽڵģ��ڸ�λ��0��Ȼ����ת��ʮ����
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


