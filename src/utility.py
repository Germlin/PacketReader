# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

import os
import types
import collections
import struct
import sys


def testBit(int_data, offset):
    '''
    测试某一位是否为1
    :param int_data: int类型的数据
    :param offset: 要测试的位，最高位为7
    :return:是1的时候返回True
    '''
    mask = 0b00000001 << offset
    return bool(int_data & mask)


def byteToInt(byte_data):
    return int(byte_data.encode('hex'), 16)





def followTCPstream(ip):
    pass
