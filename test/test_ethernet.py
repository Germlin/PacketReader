# -*- encoding=utf-8 -*-

from PyPcap.pcap import *
from PyPcap.ethernet import *
import unittest


class TestEthernet(unittest.TestCase):
    pass


class TestEthernetPacket(unittest.TestCase):
    def setUp(self):
        self.file = open(r"E:\PyPcap\test\test_pcap.pcap", 'rb')
        test_pcap = Pcap(self.file)
        test_packet = test_pcap.packets[13]
        self.test_eth_packet = EthernetPacket(test_packet)

    def testType(self):
        self.assertEqual(self.test_eth_packet.fmt_type(), 'ETH_TYPE_IP')

    def testDst(self):
        self.assertEqual(self.test_eth_packet.fmt_dst(), '28:c2:dd:1d:75:c1')

    def testSrc(self):
        self.assertEqual(self.test_eth_packet.fmt_src(), '88:25:93:37:60:84')

    def tearDown(self):
        self.file.close()


class TestEthernet(unittest.TestCase):
    def setUp(self):
        self.file = open(r"E:\PyPcap\test\test_pcap.pcap", 'rb')
        test_pcap = Pcap(self.file)
        self.test_eth = Ethernet(test_pcap)

    def testNum(self):
        self.assertEqual(len(self.test_eth.eth_packets), 19)


if __name__ == "__main__":
    unittest.main()
