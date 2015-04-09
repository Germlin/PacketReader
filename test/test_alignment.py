# -*- encoding=utf-8 -*-

__author__ = 'linyue'


import ProtocolReverse
import timeit
import random


def timer_nw():
    global seq1,seq2
    lcs,seq=ProtocolReverse.alignment.needleman_wunsch_alignment(seq1,seq2)
    return lcs,seq

def timer_sw():
    global seq1,seq2
    lcs=ProtocolReverse.alignment.smith_waterman_alignment(seq1,seq2)
    return lcs

if __name__=="__main__":

    time = 1
    tsw = tnw = 0
    while time <= 10000:
        seq1=list()
        for i in range(random.randint(10,1000)):
            seq1.append(random.choice(["A","C","G","T"]))
        #print(seq1)
        seq2=list()
        for j in range(random.randint(10,1000)):
            seq2.append(random.choice(["A","C","G","T"]))
        #print(seq2)

        tsw += timeit.timeit('timer_sw',setup="from __main__ import timer_sw;")
        tnw += timeit.timeit('timer_nw',setup="from __main__ import timer_nw;")
        print(time,tsw,tnw)

        time += 1

    print(tsw,tnw)
    # lcs, seq = timer_nw()
    # print(seq1)
    # print(seq2)
    # print(lcs)
    # for i in seq:
    #     print(i)
    #
    # print(timer_sw())
