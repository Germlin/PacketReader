# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import ProtocolReverse


def basetest():
    pass


def realtest():
    path = r"E:\快盘\毕业设计\ProtocolReverse\output\ciba.pcap\Dst_192.168.137.3_34649_Src_114.112.83.218_80_2.tcpd"
    f = open(path, 'rb')
    d = f.read()
    ttd = ProtocolReverse.tokenize.tokenization(d, text_threshold=10)
    ms=ProtocolReverse.message.Message(ttd)
    # for t in ms.token_list :
    #     if t.type=='T':
    #         print(t.data.decode('utf8'))

    print(ms.compressed(),ms.chunked(),sep='\n')
    print(ms.decompress())

if __name__ == '__main__':
    realtest()
