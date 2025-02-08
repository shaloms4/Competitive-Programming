# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution(object):
    def largestLocal(self, grid):
        n =  len(grid)
        result = [[0] * (n - 2) for _ in range (n - 2)]
        for i in range (n - 2):
            for j in range (n - 2):
                for row in range (i, i + 3):
                    for column in range (j, j + 3):
                        result [i][j] = max(result[i][j], grid[row][column])
        return result

        