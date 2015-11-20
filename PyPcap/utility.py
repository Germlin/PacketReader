# -*- encoding=utf-8 -*-

import struct


def test_bit(int_data, offset):
    """
    测试某一位是否为1。
    :param int_data: int类型的数据
    :param offset: 要测试的位，最高位为7
    :return: 是1的时候返回True
    """
    mask = 0b00000001 << offset
    return bool(int_data & mask)


def byte_to_int(byte_data):
    res = int.from_bytes(byte_data, byteorder='big', signed=False)
    return res


def get_filed(data_in, byte_offset, bit_offset, length):
    """
    获取header指定的数据域，比如第四个字节的后四位。
    :param byte_offset: 数据域开始的字节位置
    :param bit_offset: 数据域开始的位位置
    :param length: 数据域的长度，按照位计算
    :return: int类型，不足一个字节的，在高位补0，然后再转成十进制,按字节计算。
    """
    byte_length = (length - (8 - bit_offset)) // 8 + 1
    data = data_in[byte_offset:(byte_offset + byte_length)]
    mask = 2 ** (byte_length * 8 - bit_offset) - 1
    data_int = int.from_bytes(data, byteorder='big', signed=False)
    res = data_int & mask
    return res
