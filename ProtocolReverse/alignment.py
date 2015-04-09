# -*- encoding=utf-8 -*-

__author__ = 'linyue'

from numpy import *


def needleman_wunsch_alignment(seq_1, seq_2):
    """
    Needleman-Wunsch算法是用来计算两个序列的公共序列。
    :param seq_1: 要对比的序列A，要求类型为列表，元素必须重载了__eq__函数。
    :param seq_2: 要对比的序列B，要求同上。
    :return: 最长公共序列长度，最长公共序列
    """
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    mx = zeros((seq_1_len + 1, seq_2_len + 1))

    # 初始化得分矩阵
    for i in range(0, seq_1_len + 1):
        mx[i][0] = 0 - i

    for i in range(0, seq_2_len + 1):
        mx[0][i] = 0 - i

    # 计算匹配矩阵
    for i in range(1, seq_1_len + 1):
        for j in range(1, seq_2_len + 1):
            if seq_1[i - 1] == seq_2[j - 1]:
                mx[i][j] = mx[i - 1][j - 1] + 1
            else:
                mx[i][j] = max([mx[i - 1][j - 1], mx[i - 1][j], mx[i][j - 1]])

    lcs = 0
    new_seq = list()

    # 开始回溯
    i = seq_1_len
    j = seq_2_len
    while i or j:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif seq_1[i - 1] == seq_2[j - 1]:
            lcs += 1
            new_seq.append(seq_1[i - 1])
            i -= 1
            j -= 1
        else:
            t = (mx[i - 1][j - 1], mx[i - 1][j], mx[i][j - 1])
            max_value = max(t)
            index = t.index(max_value)
            if index == 0:
                i -= 1
                j -= 1
            elif index == 1:
                i -= 1
            elif index == 2:
                j -= 1

    new_seq.reverse()
    return lcs, new_seq


def smith_waterman_alignment(seq_1, seq_2):
    """
    Smith-Waterman算法，用于计算两个序列之间的距离。
    :param seq_1:
    :param seq_2:
    :return:
    """
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    mx = zeros((seq_1_len + 1, seq_2_len + 1))

    # 计算匹配矩阵
    max_score = 0
    max_i = 0
    max_j = 0
    for i in range(1, seq_1_len + 1):
        for j in range(1, seq_2_len + 1):
            if seq_1[i - 1] == seq_2[j - 1]:
                mx[i][j] = mx[i - 1][j - 1] + 2
            else:
                mx[i][j] = max([mx[i - 1][j - 1] - 1, mx[i - 1][j] - 2, mx[i][j - 1] - 2, 0])

            if mx[i][j] > max_score:
                max_score = mx[i][j]
                max_i = i
                max_j = j
    lcs = 0

    # 开始回溯
    i = max_i
    j = max_j
    while 0 != mx[i][j]:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif seq_1[i - 1] == seq_2[j - 1]:
            lcs += 1
            i -= 1
            j -= 1
        else:
            t = (mx[i - 1][j - 1], mx[i - 1][j], mx[i][j - 1])
            max_value = max(t)
            index = t.index(max_value)
            if index == 0:
                i -= 1
                j -= 1
            elif index == 1:
                i -= 1
            elif index == 2:
                j -= 1

    return lcs
