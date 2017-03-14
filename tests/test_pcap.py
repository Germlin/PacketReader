# -*- encoding=utf-8 -*-

import PacketReader
import unittest


class TestPcap(unittest.TestCase):
    def setUp(self):
        file_name = r"E:\GitHub\PyPcapAnalyzer\tests\test.pcap"
        self.packets = PacketReader.read_pcap(file_name)

    def test_packet_num(self):
        self.assertEqual(len(self.packets), 179)


class TestPacket(unittest.TestCase):
    def setUp(self):
        file_name = r"E:\GitHub\PyPcapAnalyzer\tests\test.pcap"
        self.packet = PacketReader.read_pcap(file_name)[0]

    def test_timestamp(self):
        self.assertEqual(self.packet.packet_header['TSS'], 1448157839)
        self.assertEqual(self.packet.packet_header['TSM'], 796592)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPcap('test_packet_num'))
    suite.addTest(TestPacket('test_timestamp'))
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest='suite')
