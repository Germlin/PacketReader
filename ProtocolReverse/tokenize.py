# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'

import utility
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
        assert isinstance(mes, message.Message)
        self.tpl = list()
        self.dst = mes.destination
        self.src = mes.source
        for x in mes.priority_list:
            tp = [x.type, x.variable]
            self.tpl.append(tp)

    def __eq__(self, other):
        if isinstance(other, tokenPattern):
            if self.dst != other.dst or self.src != other.dst:
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


def tokenize_by_byte(data):
    assert isinstance(data, bytes)
    token_patten = []
    data_length = len(data)
    k = 0
    while k < data_length:
        first_byte = data[k:k + 1]
        first_byte_int = utility.byte_to_int(first_byte)
        if not utility.test_bit(first_byte_int, 7):
            try:
                decode_data = first_byte.decode('ascii')
            except Exception as e:
                token_patten.append(token(first_byte, t_type='B'))
            else:
                token_patten.append(token(first_byte, t_type='T'))
            finally:
                k += 1
        elif not utility.test_bit(first_byte_int, 6):
            token_patten.append(token(first_byte, t_type='B'))
            k += 1
        else:
            i = 5
            while i > 0 and utility.test_bit(first_byte_int, i):
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
    res = list()
    data_token = tokenize_by_byte(data)
    # 将连续长度少于门限值的文字标记改成二进制标记。
    i = 0
    while i < len(data_token):
        if data_token[i].type == 'T':
            b = e = i
            while i < len(data_token) and data_token[i].type == 'T':
                e += 1
                i += 1
            if (e - b) < text_threshold:
                for x in data_token[b:e]:
                    x.type = 'B'
        i += 1

    index = begin = 0
    last_token_type = data_token[index].type
    while index <= len(data_token):
        if index == len(data_token) or data_token[index].type != last_token_type:
            merge_data = b''
            for x in data_token[begin:index]:
                merge_data = merge_data + x.data
            merge_token = token(merge_data, t_type=last_token_type)
            res.append(merge_token)
            begin = index
            if index < len(data_token):
                last_token_type = data_token[begin].type
        index += 1
    return res


def tokenize_tcp(tcp_datagram):
    assert isinstance(tcp_datagram, tcp.TcpDatagram)
    token_list = tokenization(tcp_datagram.get_data())
    t_message = message.Message(token_list, tcp_datagram.get_data(), tcp_datagram.get_dst_socket(),
                                tcp_datagram.get_src_socket())
    return t_message


if __name__ == "__main__":
    test_data_1 = 'POST'.encode() + b'\xff\xfe\xfd' + 'IP'.encode() + b'\xfc\xfb' + 'END'.encode()  # TTTTBBBTTBBTTT -> TBT
    test_data_2 = 'PUSH'.encode() + b'\xfa\xf9\xf8' + 'TH'.encode() + b'\xf7\xf6' + 'OUT'.encode()  # TTTTBBBTTBBTTT -> TBT
    test_data_3 = '中国'.encode() + b'\x03\xf2' + 'TEST'.encode()  # TTTBTTTT -> TBT
    for t in tokenize_by_byte(test_data_1):
        print(t.type, end='')
    print()
    for t in tokenize_by_byte(test_data_2):
        print(t.type, end='')
    print()
    for t in tokenize_by_byte(test_data_3):
        print(t.type, end='')
    print('\n' + '-' * 60)

    l1 = tokenization(test_data_1)
    l2 = tokenization(test_data_2)
    for t in l1:
        print(t.type, end='')
    print()
    for t in l2:
        print(t.type, end='')
    print()
    for t in tokenization(test_data_3):
        print(t.type, end='')
    print('\n' + '-' * 60)
    print(l1[0] == l2[0], l1[0] == l2[1])
