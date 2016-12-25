# -*- encoding=utf-8 -*-

import PyPcapAnalyzer
import unittest


class TestPcap(unittest.TestCase):
    def setUp(self):
        file_name = r"E:\GitHub\PyPcapAnalyzer\tests\test.pcap"
        self.packets = PyPcapAnalyzer.read_pcap(file_name)

    def test_packet_num(self):
        self.assertEqual(len(self.packets), 179)


class TestPacket(unittest.TestCase):
    def setUp(self):
        file_name = r"E:\GitHub\PyPcapAnalyzer\tests\test.pcap"
        self.packet = PyPcapAnalyzer.read_pcap(file_name)[0]


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPcap('test_packet_num'))
    return suite


if __name__ == "__main__":
    file_name = r"E:\GitHub\PyPcapAnalyzer\tests\test.pcap"
    packet = PyPcapAnalyzer.read_pcap(file_name)[0]
    print(packet)
    unittest.main(defaultTest='suite')
