# -*- encoding=utf-8 -*-

import unittest
import struct
from PyPcapAnalyzer.packet import BasicPacket


class TestBasicPacket(unittest.TestCase):
    _data_structure_ = (
        ('INT', 'I', 4),    #（‘数据域名’，‘个数+类型’，总长度）
        ('SHORT', 'H', 2),
        ('CHAR', '2B', 2),
        ('CHK', 'H', 2),
    )

    def setUp(self):
        self.packet = BasicPacket(self._data_structure_)
        self.data = struct.pack('IH2BH', 0x01020304, 0xABCD, 0x1C, 0x2D, 0x2310)

    def test_bp_parse_header(self):
        result = {
            'INT': 0x04030201,
            'SHORT': 0xCDAB,
            'CHAR': (0x1C, 0x2D),
            'CHK': 0x1023
        }
        self.packet._parse_header_(self.data)
        self.assertEqual(self.packet.header, result)

    def test_pt_hdr_len(self):
        self.assertEqual(self.packet._header_length_, 10)

    def test_check_sum(self):
        self.assertEqual(self.packet.checksum(self.data), 0)

    def tearDown(self):
        self.packet = None


if __name__ == '__main__':
    unittest.main()
