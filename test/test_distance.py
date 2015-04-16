# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import ProtocolReverse


def test():
    ma=ProtocolReverse.message.Message(data="T C G A A".encode())
    # for i in ma.token_list:
    #     print(i)
    mb=ProtocolReverse.message.Message(data="T C C G A".encode())
    mc=ProtocolReverse.message.Message(data="C C A G A".encode())
    mac=ProtocolReverse.message.MessageCluster([ma,mb])
    mcc=ProtocolReverse.message.MessageCluster([mc])
    ms=ProtocolReverse.message.MessageSet([mac,mcc])
    md=ProtocolReverse.distance.Distance(ms)
    print(md.matrix)

if __name__=="__main__":
    test()
