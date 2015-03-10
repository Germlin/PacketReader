__author__ = 'Reuynil'

from utility import *
from ip import *


class TCP:
    def __init__(self, ipDatagram):
        self.__data = ipDatagram.data
        self.fields = collections.OrderedDict()
        self.items = ("SrcPort", "DstPort", "Seq", "Ack", "Length", "Flags", "Win", "Sum", "Urp")
        index = 0
        for value in struct.unpack('!2H2L2B3H', self.__data[:20]):
            self.fields[self.items[index]] = value
            index += 1

    def getSrcPort(self):
        return self.fields["SrcPort"]

    def getDstPort(self):
        return self.fields["DstPort"]

    def getLength(self):
        return (self.fields["Length"] >> 4) * 4

    def checkSum(self):
        pass

    def getData(self):
        pass

    def getSYN(self):
        return testBit(self.fields["Flags"], 2)

    def getACK(self):
        return testBit(self.fields["Flags"], 4)

    def getFIN(self):
        return testBit(self.fields["Flags"], 0)

    class quadruple:
        pass

    @staticmethod
    def reassembleTCP(pcap):
        assert isinstance(pcap, pcap)
        IP_packet = reassembleIP(pcap)
        work_list = dict()
        for pk in IP_packet:
            assert isinstance(pk, ipDatagram)
            if pk.protocol == 'IP_PROTO_TCP':
                pk_dst_ip = pk.dst
                pk_src_ip = pk.src
                pk_tcp = TCP(pk)
                pk_dst_port = pk_tcp.getDstPort()
                pk_src_port = pk_tcp.getSrcPort()
                quadruple = (pk_dst_ip, pk_dst_port, pk_src_ip, pk_src_port)
                if quadruple in work_list:
                    work_list[quadruple].append(pk.data)
                else:
                    work_list[quadruple] = [pk.data]
        for k in work_list:
            tcp_segment_list = work_list[k]


class TcpDatagram:
    def __init__(self):
        pass


def reassembleTCP(pcap, src, dst):
    assert isinstance(pcap, pcap)
    IP_packet = reassembleIP(pcap)
    temp_packet = list()
    for pk in IP_packet:
        assert isinstance(pk, ipDatagram)
        if pk.protocol == 'IP_PROTO_TCP':
            temp_packet.append(pk.getData())

