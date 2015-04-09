# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import tokenize
import re
import gzip
import tcp
from abc import ABCMeta, abstractclassmethod


class Message(object):

    def __init__(self, t_token_list, t_destination=None, t_source=None):
        """
        消息包括记号列表和方向。
        """
        self.token_list = t_token_list
        self.destination = t_destination
        self.source = t_source
        self.data = self.get_data()

    def __eq__(self, other):
        return True if self.data == other.data else False

    def get_data(self):
        data = b''
        for t in self.token_list:
            data += t.data
        return data

    def compressed(self):
        """
        测试消息是否包含一些关键词，如 gzip，如果有，则认为这个消息是的内容是经过压缩的。
        返回： 如果包含关键词，返回关键词所在的token在self.token_list中的位置
              如果不包含，返回None
        """
        for t in self.token_list:
            assert isinstance(t, tokenize.Token)
            if t.type == 'T':
                td = t.data.decode('utf8')
                re_res = re.search(r'gzip', td)
                if re_res is not None:
                    return self.token_list.index(t)
        return None

    def chunked(self):
        for t in self.token_list:
            assert isinstance(t, tokenize.Token)
            if t.type == 'T':
                td = t.data.decode('utf8')
                re_res = re.search(r'chunked', td)
                if re_res is not None:
                    return self.token_list.index(t)
        return None

    def decompress(self):
        """
        前置条件：message是有压缩的。
        对经过压缩的消息进行解压缩，分成两步：
        1、判断数据是不是可变长度的；
        2、将gzip数据合并起来；
        3、对gzip数据进行解压缩；
        返回： 如果解压成功，返回bytes类型的解压数据。
              如果解压失败，返回None
        """
        compress_begin = self.compressed() + 1
        compress_len = -1
        if self.chunked():
            length = self.token_list[compress_begin].data.decode()
            len_str = re.search(r'^\w+', length).group()
            compress_len = int(len_str, 16)
            compress_begin += 1
        merge_data = b''
        for t in self.token_list[compress_begin:]:
            merge_data += t.data
        try:
            uncompress_data = gzip.decompress(merge_data[:compress_len])
        except TypeError:
            return None
        return uncompress_data

    def get_token_pattern(self):
        return TokenPattern(self)


class Character(metaclass=ABCMeta):
    """
    在PR中，我们使用dict来表示消息集合，集合的key就是character，value是list类型，list类型的元素是Message.即：

    dict.key.type==subclass of character,
    dict.value.type==list,
    dict.value.item.type==Message。

    同一个消息集合里的Message具有共同的特点，这个特点由character决定，character是一个类对象，这个类对象描述了
    该集合里面Message具有的特征，character要求具有：

    __eq__(self,other)、__hash__(self)和get_character(self,message)函数以保证：

    1.message可以获取到该集合需要的特性；

    2.这个特性可以用作dict的key。
    """

    @abstractclassmethod
    def __init__(self, message):
        pass

    @abstractclassmethod
    def __eq__(self, other):
        pass

    @abstractclassmethod
    def __hash__(self):
        pass


class Direction(Character):
    def __init__(self, message):
        super().__init__(message)
        assert isinstance(message, Message)
        self.d = message.destination
        self.s = message.source

    def __eq__(self, other):
        return True if self.d == other.d and self.s == other.s else False

    def __hash__(self):
        sd = self.d.replace('.', '').replace(':', '')
        ss = self.s.replace('.', '').replace(':', '')
        return int(ss + sd)


class TokenPattern(Character):
    def __init__(self, mes):
        super().__init__(mes)
        self.tpl = list()
        for x in mes.token_list:
            self.tpl.append(x.type)

    def __eq__(self, other):
        if isinstance(other, TokenPattern):
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

    def __hash__(self):
        t = 0
        for i in self.tpl:
            if i == 'T':
                t = t*10 + 1
            else:
                t = t*10 + 0
        return t


class MessageSet:
    def __init__(self, characteristics):
        """
        消息集合，集合里的元素类型为Message，同一个消息集合里的Message具有共同的特点，这个特点由character
        决定，character是一个类对象，这个类对象描述了该集合里面Message具有的特征，character要求具有一个
        __eq__(self,other)函数和一个get_character(self,message)函数以保证：1.message可以获取到该集合
        需要的特性；2.这个特性可以对比，以确定消息是否属于这个集合。
        参数：
            characteristics是一个类对象，代表了这个消息集的特征。
            在不同的聚类阶段，这个参数的类型可以不同，比如由记号模式变成长度等等。
        """
        self.characteristics = characteristics




def tokenize_tcp(tcp_datagram):
    assert isinstance(tcp_datagram, tcp.TcpDatagram)
    token_list = tokenize.tokenization(tcp_datagram.get_data())
    t_message = Message(token_list, tcp_datagram.get_dst_socket(),
                                tcp_datagram.get_src_socket())
    return t_message
