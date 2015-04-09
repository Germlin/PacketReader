# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import utility


class Token:
    SEPARATOR = [" ", "\r", "\n"]  # 分隔符

    def __init__(self, t_data, t_type='B', t_variable=True, t_decoded_data=None):
        self.data = t_data
        self.type = t_type
        self.variable = t_variable
        self.separator = True if t_decoded_data in self.SEPARATOR else False

    # def __eq__(self, other):
    #     if isinstance(other, Token):
    #         if self.type == other.type and self.variable == other.variable:
    #             return True
    #         else:
    #             return False
    #     else:
    #         raise TypeError()

    def __str__(self):
        return "type:\t" + self.type + "\ndata:\t" + repr(self.data)


def tokenize_by_byte(data):
    assert isinstance(data, bytes)
    token_patten = []
    if len(data) == 0:
        return token_patten
    data_length = len(data)
    k = 0
    while k < data_length:
        first_byte = data[k:k + 1]
        first_byte_int = utility.byte_to_int(first_byte)
        if not utility.test_bit(first_byte_int, 7):
            try:
                decode_data = first_byte.decode('ascii')
            except UnicodeDecodeError:
                token_patten.append(Token(first_byte, t_type='B'))
            else:
                token_patten.append(Token(first_byte, t_type='T', t_decoded_data=decode_data))
            finally:
                k += 1
        elif not utility.test_bit(first_byte_int, 6):
            token_patten.append(Token(first_byte, t_type='B'))
            k += 1
        else:
            i = 5
            while i > 0 and utility.test_bit(first_byte_int, i):
                i -= 1
            if i < 2:
                token_patten.append(Token(first_byte, t_type='B'))
                k += 1
            else:
                remain_byte_length = 6 - i
                try:
                    remain_byte = data[k + 1:k + remain_byte_length + 1]
                except UnicodeDecodeError:
                    token_patten.append(Token(first_byte, t_type='B'))
                    k += 1
                else:
                    full_byte = first_byte + remain_byte
                    try:
                        decode_data = full_byte.decode('utf8')
                    except UnicodeDecodeError:
                        token_patten.append(Token(first_byte, t_type='B'))
                        k += 1
                    else:
                        token_patten.append(Token(full_byte, t_type='T', t_decoded_data=decode_data))
                        k = k + remain_byte_length + 1
    return token_patten


def tokenization(data, text_threshold=4):
    res = list()
    if len(data) == 0:
        return res
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

    # 将连续的文本类型或二进制数据合并。
    index = begin = 0
    last_token_type = data_token[begin].type
    while index <= len(data_token):
        # 读完数据、遇到分隔符、数据类型改会导致数据的合并。
        if index == len(data_token) or data_token[index].separator or data_token[index].type != last_token_type:
            if index < len(data_token) and data_token[index].separator:
                # 由于分隔符导致的数据合并，会把多个分隔符合并到分隔符前的一段数据，如回车换行符（CRLF），会被合并成“data-CRLF”。
                while index < len(data_token) and data_token[index].separator:
                    index += 1
            merge_data = b''
            for x in data_token[begin:index]:
                merge_data = merge_data + x.data
            merge_token = Token(merge_data, t_type=last_token_type)
            res.append(merge_token)
            begin = index
            if index < len(data_token):
                last_token_type = data_token[begin].type
        index += 1
    return res
