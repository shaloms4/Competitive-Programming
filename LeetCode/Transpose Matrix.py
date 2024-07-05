class Solution(object):
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        transpose_matrix = [[0] * m for _ in range (n)]
        for i in range(m):
            for j in range(n):
                transpose_matrix[j][i] = matrix[i][j]
        return transpose_matrix