__author__ = 'Reuynil'

from utility import *
from ip import *


class TCP:
    def __init__(self, ipDatagram):
        self.data = ipDatagram.data
        self.fields = {"Sport": self.data[0:4],
                       "Dport": self.data[4:8],
                       "Seq": getFiled(self.data, 4, 0, 32),
                       "Ack": getFiled(self.data, 8, 0, 32),
                       "Length": getFiled(self.data, 12, 0, 4),
                       "Flags": None,
                       "Win": None,
                       "Sum": None,
                       "Urp": None,
                       "Options": None}

    def getData(self):
        pass


def reassembleTCP(pcap):
    assert isinstance(pcap, pcap)
    IP_packet = reassembleIP(pcap)


