# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'

from utility import *
import tcp
import message


class token:
    def __init__(self, t_data, t_type='B', t_variable=True):
        self.data = t_data
        self.type = t_type
        self.variable = t_variable

    def __eq__(self, other):
        if isinstance(other, token):
            if self.type == other.type and self.variable == other.variable:
                return True
            else:
                return False
        else:
            raise TypeError()

    def __str__(self):
        return "type:\t" + self.type + "\ndata:\t" + repr(self.data)


class tokenPattern:
    def __init__(self, mes):
        assert isinstance(mes, message.message)
        self.tpl = list()
        for x in mes.priority_list:
            tp = [x.type, x.variable]
            self.tpl.append(tp)

    def __eq__(self, other):
        if isinstance(other, tokenPattern):
            x_l = len(self.tpl)
            y_l = len(other.tpl)
            if x_l != y_l:
                return False
            else:
                index = 0
                while index < x_l:
                    if self.tpl[index] != other.tpl[index]:
                        return False
                    index += 1
            return True
        else:
            raise TypeError()


def data_tokenization(data):
    """
    根据utf-8编码规则判断数据是否为字符，是的话将对应字段记为T，不是记为B。
    :param data:字符串，不经过任何编码。
    :return:一个列表，元素是标记。
    """
    assert isinstance(data, bytes)
    token_patten = []
    data_length = len(data)
    k = 0
    while k < data_length:
        first_byte = data[k:k + 1]
        first_byte_int = byte_to_int(first_byte)
        if not test_bit(first_byte_int, 7):
            try:
                decode_data = first_byte.decode('ascii')
            except Exception as e:
                token_patten.append(token(first_byte, t_type='B'))
            else:
                token_patten.append(token(first_byte, t_type='T'))
            finally:
                k += 1
        elif not test_bit(first_byte_int, 6):
            token_patten.append(token(first_byte, t_type='B'))
            k += 1
        else:
            i = 5
            while i > 0 and test_bit(first_byte_int, i):
                i -= 1
            if i < 2:
                token_patten.append(token(first_byte, t_type='B'))
                k += 1
            else:
                remain_byte_length = 6 - i
                try:
                    remain_byte = data[k + 1:k + remain_byte_length + 1]
                except Exception as e:
                    token_patten.append(token(first_byte, t_type='B'))
                    k += 1
                else:
                    full_byte = first_byte + remain_byte
                    try:
                        decode_data = full_byte.decode('utf8')
                    except Exception as e:
                        token_patten.append(token(first_byte, t_type='B'))
                        k += 1
                    else:
                        token_patten.append(token(full_byte, t_type='T'))
                        k = k + remain_byte_length + 1
    return token_patten


def tokenization(data, text_threshold=3):
    """
    tokenize the message,
    :param data: type: bytes, the data to be tokenize.
    :param text_threshold: type: int, the minimum length of the text field.
    :return: type: list, the element of the list is token.
    """
    res = list()
    data_token = data_tokenization(data)
    index = begin = 0
    last_token_type = data_token[index].type
    while index <= len(data_token):
        if index == len(data_token) or data_token[index].type != last_token_type:
            if not (last_token_type == 'B' and index - begin < text_threshold):
                merge_data = b''
                for x in data_token[begin:index]:
                    merge_data = merge_data + x.data
                merge_token = token(merge_data, t_type=last_token_type)
                res.append(merge_token)
                begin = index
                last_token_type = data_token[index].type
        index += 1
    return res


def tokenize_tcp(tcp_datagram_list):
    """
    tokenize each datagram of the tcp_datagram_list.
    :param tcp_datagram_list: a list of tcp datagram.
    :return: a list contains message.
    """
    res = list()
    for x in tcp_datagram_list:
        assert isinstance(x, tcp.TcpDatagram)
        token_list = tokenization(x.get_data())
        t_message = message.message(token_list, x.get_data(), x.get_dst_socket(), x.get_src_socket())
        res.append(t_message)
    return res


if __name__ == "__main__":
    f = open('test_text.txt', 'rb')
    data = f.read()
    token_patten_list = tokenization(data)
    print('=' * 60)
    for item in token_patten_list:
        print(item)
