# -*- encoding=utf-8 -*-

from PyPcapAnalyzer.pcap import Pcap, Packet
import unittest


class TestPcap(unittest.TestCase):
    def setUp(self):
        self.file = open(r"E:\PyPcap\test\test_pcap.pcap", 'rb')
        self.test_file = Pcap(self.file)

    def test_header(self):
        res = {
            'Magic': 0xA1B2C3D4,
            'Major': 0x02,
            'Minor': 0x04,
            'ThisZone': 0x0,
            'SignFigs': 0x0,
            'SnapLen': 0x00040000,
            'LinkType': 0x01
        }
        self.assertEqual(self.test_file.header, res)

    def test_packet_num(self):
        self.assertEqual(self.test_file.packets_num, 333)

    def tearDown(self):
        self.test_file = None


class TestPacket(unittest.TestCase):
    def setUp(self):
        self.file = open(r"E:\PyPcap\test\test_pcap.pcap", 'rb')
        self.test_file = Pcap(self.file)
        self.test_packet = self.test_file.packets[0]

    def test_packet_header(self):
        res = {
            'TimestampSec': 0x5651228F,
            'TimestampMSe': 0x0005F3F8,
            'CaptureLength': 0x56,
            'Length': 0x56,
        }

    def tearDown(self):
        self.test_file = None


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPcap, 'test_header')
    suite.addTest(TestPcap, 'test_packet_num')
    suite.addTest(TestPacket, 'test_packet_header')
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest='suite')
