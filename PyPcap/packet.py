# -*- encoding=utf-8 -*-

import struct


class BasicPacket(object):
    def __init__(self, _hdr_st):
        self._header_structure_ = _hdr_st
        self._header_length_ = 0
        for x in self._header_structure_:
            self._header_length_ += x[2]

    def parse(self, data):
        res = {}
        fmt = ''
        for x in self._header_structure_:
            fmt = fmt + x[1]
        lst = struct.unpack(fmt, data)
        index = 0
        for x in self._header_structure_:
            res[x[0]] = lst[index]
            index += 1
        return res