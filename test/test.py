# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import ProtocolReverse

def realtest():
    i = 0
    l=list()
    while i < 7:
        path = r"C:\Users\Reuynil\Desktop\15032801.pcap\接收\都有\Dst_192.168.137.3_56119_Src_58.68.226.69_80_"+str(i)+".tcpd"
        i=i+1
        f = open(path, 'rb')
        d = f.read()
        ttd = ProtocolReverse.tokenize.tokenization(d, text_threshold=10)
        ms=ProtocolReverse.message.Message(ttd)
        l.append(ms.decompress())
    i=0
    for t in l:
        path=r"C:\Users\Reuynil\Desktop\15032801.pcap\ " + str(i) + ".txt"
        f=open(path,'wb')
        f.write(t)
        i = i+1


    # print(ms.compressed(),ms.chunked(),sep='\n')
    # print()

if __name__ == '__main__':
    realtest()
