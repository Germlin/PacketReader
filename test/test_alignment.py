# -*- encoding=utf-8 -*-

__author__ = 'linyue'


import ProtocolReverse


if __name__=="__main__":
    seq1=["T","A","C","G","C","G","A"]
    seq2=["A","G","C","G","C","T"]

    lcs,seq=ProtocolReverse.alignment.needleman_wunsch_alignment(seq1,seq2)
    print(lcs)
    for i in seq:
        print(i)
