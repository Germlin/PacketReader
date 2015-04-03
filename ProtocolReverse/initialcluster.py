# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import message


def cluster_by_direction(message_list):
    """
    将消息按照方向进行分类。
    :param message_list: 一个元素为message的list
    :return:按照
    """
    res = dict()
    for t in message_list:
        direction = message.Direction(t)
        if dir not in res.keys():
            res[direction] = list()
        res[direction].append(t)
    return res


def initial_cluster(message_list):
    res = dict()
    for x in message_list:
        assert isinstance(x, message.Message)
        tp = x.get_token_pattern()
        if tp not in res.keys():
            res[tp] = list()
        res[tp].append(x)
    return res
