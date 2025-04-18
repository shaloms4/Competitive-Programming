# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sub_box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or board[r][c] in cols[c] or board[r][c] in sub_box[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sub_box[(r // 3, c // 3)].add(board[r][c])
        return True

                