# -*- encoding=utf-8 -*-

import struct


class BasicPacket(object):
    def __init__(self, _hdr_st_):
        self._header_structure_ = _hdr_st_
        self._header_length_ = 0
        for x in self._header_structure_:
            self._header_length_ += x[2]
        self.header = {}

    def _parse_header_(self, data, order='B'):
        if order == 'B':
            fmt = '!'
        else:
            fmt = ''
        for x in self._header_structure_:
            fmt = fmt + x[1]
        lst = struct.unpack(fmt, data)
        index = 0
        for x in self._header_structure_:
            if len(x[1]) == 1 or x[1][1] == 's':
                self.header[x[0]] = lst[index]
                index += 1
            else:
                ls_len = int(x[1][0])
                self.header[x[0]] = lst[index:index + ls_len]
                index += ls_len

    @staticmethod
    def checksum(data):
        check_sum = 0
        length = len(data)
        i = 0
        while i < length:
            check_sum += struct.unpack('!H', data[i:i + 2])[0]
            i += 2
        check_sum = (check_sum >> 16) + (check_sum & 0xffff)
        return check_sum ^ 0xffff

    @staticmethod
    def print_ip(data):
        s = list()
        for i in data:
            s.append(oct(i))
        return str(".".join(s))


class PacketTypeError(Exception):
    pass
