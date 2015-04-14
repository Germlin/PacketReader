# -*- encoding=utf-8 -*-

__author__ = 'linyue'

import alignment
import numpy


class Distance:
    def __init__(self, message_set):
        self.set = message_set
        self.cluster_num = self.set.size()
        self.matrix = numpy.zeros((self.cluster_num, self.cluster_num))
        self.min = 0
        self.min_index = (0, 0)
        self._compute_distance_matrix()

    @staticmethod
    def _compute_distance(c1, c2):
        c1_num = c1.size()
        c2_num = c2.size()
        score = 0
        for i in c1:
            for j in c2:
                score += alignment.smith_waterman_alignment(i.token_list, j.token_list)
        return score / (c1_num + c2_num)

    def _compute_distance_matrix(self):
        for i in range(0, self.cluster_num):
            for j in range(i, self.cluster_num):
                self.matrix[i][j] = self._compute_distance(self.set[i], self.set[j])
                if self.matrix[i][j] < self.min:
                    self.min = self.matrix[i][j]
                    self.min_index = (i, j)

    def min(self):
        return (self.min, self.min_index)
