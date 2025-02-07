# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        transpose_matrix = [[0] * row for _ in range (column)]
        for i in range(row):
            for j in range(column):
                transpose_matrix[j][i] = matrix[i][j]
        return transpose_matrix