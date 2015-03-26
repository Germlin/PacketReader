# -*- encoding=utf-8 -*-

__author__ = 'Reuynil'

import message
import tokenize


def initial_cluster(message_list):
    res = dict()
    for x in message_list:
        assert isinstance(x, message.Message)
        dst = x.destination
        src = x.source

        tp = tokenize.tokenPattern(x)
    return res
