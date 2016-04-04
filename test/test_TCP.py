# -*- encoding=utf-8 -*-

from PyPcap.tcp import *
import unittest


class TestTCPPacket(unittest.TestCase):
    def setUp(self):
        self.file = open(r"test_TCP.pcap", 'rb')
        test_pcap = Pcap(self.file)
        test_packet = test_pcap.packets[0]
        test_eth_packet = EthernetPacket(test_packet)
        test_ip_packet = IPPacket(test_eth_packet)
        self.test_tcp_packet = TCPPacket(test_ip_packet)

    def testSRC(self):
        self.assertEqual(self.test_tcp_packet.src_port,21)

    def testDST(self):
        self.assertEqual(self.test_tcp_packet.dst_port,3624)

    def testHeaderLength(self):
        self.assertEqual(self.test_tcp_packet.header_length,20)

    def testSEQ(self):
        self.assertEqual(self.test_tcp_packet.seq,2861600412)

    def testACKSEQ(self):
        self.assertEqual(self.test_tcp_packet.ack_seq,260214837)

    def testSYN(self):
        self.assertEqual(self.test_tcp_packet.syn, 0)

    def testACK(self):
        self.assertEqual(self.test_tcp_packet.ack, 1)

    def testPSH(self):
        self.assertEqual(self.test_tcp_packet.psh, 1)

    def testWIN(self):
        self.assertEqual(self.test_tcp_packet.win, 46)

    def testDataLength(self):
        self.assertEqual(len(self.test_tcp_packet.data), 189)

    def testChecksum(self):
        self.assertEqual(self.test_tcp_packet.check_sum,0)

    def tearDown(self):
        self.file.close()


class TestTCPReassemble(unittest.TestCase):
    def setUp(self):
        self.file = open(r"test_tcp_reassemble.pcap", 'rb')
        test_pcap = Pcap(self.file)
        ethernet_packets = []
        for p in test_pcap.packets:
            ethernet_packets.append(EthernetPacket(p))
        ip_packets = []
        for p in ethernet_packets:
            ip_packets.append(IPPacket(p))
        self.reassemble_tcp = tcp_reassemble(ip_packets)

    def testTCPReassemble(self):
        self.assertEqual(len(self.reassemble_tcp),10)

    def tearDown(self):
        self.file.close()


if __name__ == '__main__':
    unittest.main()
