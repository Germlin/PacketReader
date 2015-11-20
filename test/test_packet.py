# -*- encoding=utf-8 -*-

import unittest
import struct
from PyPcap.packet import BasicPacket


class TestBasicPacket(unittest.TestCase):
    _data_structure_ = (
        ('INT', 'I', 4),
        ('SHORT', 'H', 2),
        ('CHAR', 'B', 1),
        ('STRING', '4s', 4),
    )

    def setUp(self):
        self.packet = BasicPacket(self._data_structure_)
        self.data = struct.pack('!IHB4s', 0x01020304, 0xABCD, 0x1C, b'ABCD')

    def test_bp_parse_header(self):
        result = {
            'INT': 0x04030201,
            'SHORT': 0xCDAB,
            'CHAR': 0x1C,
            'STRING': b'ABCD'
        }
        self.packet._parse_header_(self.data)
        self.assertEqual(self.packet.header, result)

    def test_pt_hdr_len(self):
        self.assertEqual(self.packet._header_length_, 11)

    def test_pt_print_header(self):
        self.packet._parse_header_(self.data)
        self.assertEqual(self.packet.print_header(), "xx")

    def tearDown(self):
        self.packet = None


if __name__ == '__main__':
    unittest.main()
