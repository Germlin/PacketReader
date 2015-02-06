# -*- encoding=cp936 -*-

__author__ = 'Reuynil'


class Text:
    def __init__(self, string_data):
        self.data = string_data
        print type(self.data), repr(self.data)

    def __str__(self):
        return self.data.decode('utf8').encode('gbk')


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
        first_byte_int = byteToInt(first_byte)
        if not testBit(first_byte_int, 7):
            try:
                decode_data = first_byte.decode('ascii')
            except Exception, e:
                token_patten.append('B')
            else:
                token_patten.append(Text(first_byte))
            finally:
                k += 1
        elif not testBit(first_byte_int, 6):
            token_patten.append('B')
            k += 1
        else:
            i = 5
            while i > 0 and testBit(first_byte_int, i):
                i -= 1
            if i < 2:
                token_patten.append('B')
                k += 1
            else:
                remain_byte_length = 6 - i
                try:
                    remain_byte = data[k + 1:k + remain_byte_length + 1]
                except Exception, e:
                    token_patten.append('B')
                    k += 1
                else:
                    full_byte = first_byte + remain_byte
                    try:
                        decode_data = full_byte.decode('utf8')
                    except Exception, e:
                        token_patten.append('B')
                        k += 1
                    else:
                        token_patten.append(Text(full_byte))
                        k = k + remain_byte_length + 1
    return token_patten


if __name__ == "__main__":
    f = open('text.txt', 'rb')
    data = f.read()
    print data.encode('hex')
    token = tokenization(data)
    print '=' * 60
    for item in token:
        print item