# -*- encoding=utf-8 -*-


from PyPcapAnalyzer.ip import *
import unittest


class TestIPPacket(unittest.TestCase):
    def setUp(self):
        self.file = open(r"test_ping_ip_reassemble.pcap", 'rb')
        test_pcap = Pcap(self.file)
        test_packet = test_pcap.packets[0]
        test_eth_packet = EthernetPacket(test_packet)
        self.test_ip_packet = IPPacket(test_eth_packet)

    def testSource(self):
        self.assertEqual(self.test_ip_packet.fmt_src, "172.18.158.159")

    def testDestination(self):
        self.assertEqual(self.test_ip_packet.fmt_dst, "202.116.64.8")

    def testProtocol(self):
        self.assertEqual(self.test_ip_packet.fmt_protocol, 'IP_PROTO_ICMP')

    def testFragment(self):
        self.assertEqual(self.test_ip_packet.more_fragment, True)

    def testTotalLength(self):
        self.assertEqual(self.test_ip_packet.total_length, 1500)

    def testHeaderLength(self):
        self.assertEqual(self.test_ip_packet.header_length, 20)

    def testDataLength(self):
        self.assertEqual(len(self.test_ip_packet.data), 1480)

    def tearDown(self):
        self.file.close()


class TestIPReassemble(unittest.TestCase):
    def setUp(self):
        self.file = open(r"test_ping_ip_reassemble.pcap", 'rb')
        test_pcap = Pcap(self.file)
        test_ethernet = Ethernet(test_pcap)
        self.test_ip_datagrams = ip_reassemble(test_ethernet.packets)

    def testIPReassemble(self):
        self.assertEqual(len(self.test_ip_datagrams), 4)
        self.assertEqual(len(self.test_ip_datagrams[0].data), 10248)

    def tearDown(self):
        self.file.close()


if __name__ == '__main__':
    unittest.main()
