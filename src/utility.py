# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

import os
import types
import collections
import struct
import sys
import base64

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
    res = int.from_bytes(byte_data, byteorder='big', signed=False)
    bd = base64.b16encode(byte_data)
    return res


def getFiled(dataIn, byteOffset, bitOffset, length):
    '''
    获取header指定的数据域，比如第四个字节的后四位。
    Example:
        If the data is 6128 (two byte in hex)，getFiled(data,0,0,8) will return 97(in decimal).
        Because the arguments (0,0,8) mean the first byte of the data (61), the value of 61 in hex is 97 in decimal.
    :param byteOffset: the begin position of the field in data. 0 means the filed begins with the first byte.
    :param bitOffset: 数据域开始的位位置
    :param length: 数据域的长度，按照bit计算
    :return:int类型，不足一个字节的，在高位补0，然后再转成十进制,按字节计算
    '''
    byteLength = (length - (8 - bitOffset)) // 8 + 1
    data = dataIn[byteOffset:(byteOffset + byteLength)]
    mask = 2 ** (byteLength * 8 - bitOffset) - 1
    data_int = int(base64.b16encode(data), 16)
    res = data_int & mask
    return res


def followTCPstream(ip):
    pass
