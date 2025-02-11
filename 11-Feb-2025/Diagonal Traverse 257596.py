# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []
        cur_row = 0
        cur_col = 0
        up = True
        while len(result) != rows * cols:
            if up:
                while cur_row >= 0 and cur_col < cols:
                    result.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                up = False
            else:
                while cur_col >= 0 and cur_row < rows:
                    result.append(mat[cur_row][cur_col])
                    cur_col -= 1
                    cur_row += 1
                if cur_row == rows:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                up = True
        return result
        