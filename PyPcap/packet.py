# -*- encoding=utf-8 -*-

import struct
import base64

class BasicPacket(object):
    def __init__(self, _hdr_st_):
        self._header_structure_ = _hdr_st_
        self._header_length_ = 0
        for x in self._header_structure_:
            self._header_length_ += x[2]
        self.header = {}

    def _parse_header_(self, data):
        fmt = ''
        for x in self._header_structure_:
            fmt = fmt + x[1]
        lst = struct.unpack(fmt, data)
        index = 0
        for x in self._header_structure_:
            self.header[x[0]] = lst[index]
            index += 1

    def print_header(self):
        res = ''
        for key in self.header:
            res = res + key.ljust(16) + str(type(self.header[key])) + '\n'
        return res
