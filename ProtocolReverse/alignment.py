# -*- encoding=utf-8 -*-

__author__ = 'linyue'

from numpy import *


def needleman_wunsch_alignment(seq_1, seq_2):
    """

    :param seq_1:
    :param seq_2:
    :return:
    """
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    mx = zeros((seq_1_len + 1, seq_2_len + 1))

    # 计算匹配矩阵
    for i in range(1, seq_1_len + 1):
        for j in range(1, seq_2_len + 1):
            if seq_1[i - 1] == seq_2[j - 1]:
                mx[i][j] = mx[i - 1][j - 1] + 1
            else:
                mx[i][j] = max(mx[i - 1][j - 1], mx[i - 1][j], mx[i][j - 1])

    res_seq1=list()
    res_seq2=list()

    # 开始回溯
    i = seq_1_len
    j = seq_2_len
    while not (i == 0 and j == 0):
        if seq_1[i - 1] == seq_2[j - 1]:
            i -= 1
            j -= 1
        elif i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            t = (mx[i - 1][j - 1], mx[i - 1][j], mx[j - 1][i])
            max_value = max(t)
            index = t.index(max_value)
            if index == 0:
                i -= 1
                j -= 1
            elif index == 1:
                i -= 1
            elif index == 2:
                j -= 1





