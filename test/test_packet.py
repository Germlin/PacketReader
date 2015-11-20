# -*- encoding=utf-8 -*-

import unittest
import struct
from PyPcap import packet as pt


class TestBasicPacket(unittest.TestCase):
    _data_structure = (
        ('INT', 'I', 4),
        ('SHORT', 'H', 2),
        ('CHAR', 'B', 1),
        ('STRING', '4s', 4),
    )

    def setUp(self):
        self.packet = pt.BasicPacket(self._data_structure)

    def test_pt_parse(self):
        data = struct.pack('!IHB4s', 0x01020304, 0xABCD, 0x1C, b'ABCD')
        result = {
            'INT': 0x04030201,
            'SHORT': 0xCDAB,
            'CHAR': 0x1C,
            'STRING': b'ABCD'
        }
        self.assertEqual(self.packet.parse(data), result)

    def test_pt_hdr_len(self):
        self.assertEqual(self.packet._header_length, 11)

    def tearDown(self):
        self.packet = None


if __name__ == '__main__':
    unittest.main()
