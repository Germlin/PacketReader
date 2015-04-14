# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import tokenize
import re
import gzip
from abc import ABCMeta, abstractclassmethod


class Character(metaclass=ABCMeta):
    """
    在PR中，我们使用dict来表示消息集合，集合的key就是character，value是list类型，list类型的元素是Message.即：

    dict.key.type==subclass of character,
    dict.value.type==list,
    dict.value.item.type==Message。

    同一个消息集合里的Message具有共同的特点，这个特点由character决定，character是一个类对象，这个类对象描述了
    该集合里面Message具有的特征，character要求具有：

    __eq__(self,other)、__hash__(self)函数以保证：特性可以用作dict的key。
    """

    @abstractclassmethod
    def __eq__(self, other):
        pass

    @abstractclassmethod
    def __hash__(self):
        pass


class Direction(Character):
    def __init__(self, dst, src):
        self.d = dst
        self.s = src

    def __eq__(self, other):
        return True if self.d == other.d and self.s == other.s else False

    def __hash__(self):
        sd = self.d.replace('.', '').replace(':', '')
        ss = self.s.replace('.', '').replace(':', '')
        return int(ss + sd)


class TokenPattern(Character):
    def __init__(self, token_list):
        self.tpl = list()
        for x in token_list:
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
                t = t * 10 + 1
            else:
                t = t * 10 + 0
        return t


class Message:
    def __init__(self, tcp_datagram):
        self.destination = tcp_datagram.get_dst_socket
        self.source = tcp_datagram.get_dst_socket
        self.data = tcp_datagram.get_data()
        self.token_list = tokenize.tokenization(self.data)

    def __eq__(self, other):
        return True if self.data == other.data else False

    def direction(self):
        return Direction(self.destination, self.source)

    def pattern(self):
        return TokenPattern(self.token_list)

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


class MessageSet:
    def __init__(self, cluster_list):
        """
        消息集合，集合里的元素类型为MessageCluster，同一个消息集合里的MessageCluster具有共同的特征。
        """
        self.cluster_list = cluster_list
        self.index = 0

    def size(self):
        return len(self.cluster_list)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.cluster_list[self.index + 1]

    def __getitem__(self, item):
        return self.cluster_list[item]


class MessageCluster:
    def __init__(self, message_list):
        self.set = message_list
        self.index = 0

    def __iter__(self):
        return set

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.set[self.index + 1]

    def size(self):
        return len(self.set)
