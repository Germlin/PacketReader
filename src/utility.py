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
    ����ĳһλ�Ƿ�Ϊ1
    :param int_data: int���͵�����
    :param offset: Ҫ���Ե�λ�����λΪ7
    :return:��1��ʱ�򷵻�True
    '''
    mask = 0b00000001 << offset
    return bool(int_data & mask)

def byteToInt(byte_data):
    res = int.from_bytes(byte_data, byteorder='big', signed=False)
    bd = base64.b16encode(byte_data)
    return res


def getFiled(dataIn, byteOffset, bitOffset, length):
    '''
    ��ȡheaderָ���������򣬱�����ĸ��ֽڵĺ���λ��
    Example:
        If the data is 6128 (two byte in hex)��getFiled(data,0,0,8) will return 97(in decimal).
        Because the arguments (0,0,8) mean the first byte of the data (61), the value of 61 in hex is 97 in decimal.
    :param byteOffset: the begin position of the field in data. 0 means the filed begins with the first byte.
    :param bitOffset: ������ʼ��λλ��
    :param length: ������ĳ��ȣ�����bit����
    :return:int���ͣ�����һ���ֽڵģ��ڸ�λ��0��Ȼ����ת��ʮ����,���ֽڼ���
    '''
    byteLength = (length - (8 - bitOffset)) // 8 + 1
    data = dataIn[byteOffset:(byteOffset + byteLength)]
    mask = 2 ** (byteLength * 8 - bitOffset) - 1
    data_int = int(base64.b16encode(data), 16)
    res = data_int & mask
    return res


def followTCPstream(ip):
    pass
