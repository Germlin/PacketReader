# -*- encoding=cp936 -*-

__author__ = 'Reuynil'


def testBit(int_data, offset):
    mask = 1 << offset
    return bool(int_data & mask)


def byteToInt(byte_data):
    return int(byte_data.encode('hex'), 16)


def tokenization(data):
    '''
    根据utf-8编码规则判断数据是否为字符，是的话将对应字段记为T，不是记为B。
    :param data:字符串，不经过任何编码。
    :return:一个列表，元素是标记。
    '''
    token_patten = []
    data_length = len(data)
    k = 0
    while k < data_length:
        first_byte = data[k]
        if testBit(byteToInt(first_byte), 7):
            try:
                first_byte.encode('ascii')
            except Exception, e:
                token_patten.append('B')
            token_patten.append('T')
        else:
            i = 6
            while testBit(byteToInt(first_byte), i):
                i = i - 1



