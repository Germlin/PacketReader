# -*- encoding=cp936 -*-

__author__ = 'Reuynil'


def testBit(int_data, offset):
    mask = 1 << offset
    return bool(int_data & mask)


def byteToInt(byte_data):
    return int(byte_data.encode('hex'), 16)


def tokenization(data):
    '''
    ����utf-8��������ж������Ƿ�Ϊ�ַ����ǵĻ�����Ӧ�ֶμ�ΪT�����Ǽ�ΪB��
    :param data:�ַ������������κα��롣
    :return:һ���б�Ԫ���Ǳ�ǡ�
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



