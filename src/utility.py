# -*- encoding=cp936 -*-

__author__ = 'Reuynil'

import os
import types
import collections
import struct
import sys


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
    return int(byte_data.encode('hex'), 16)





def followTCPstream(ip):
    pass
