# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        stack = []
        for i in range(rowIndex + 1):
            if not stack:
                stack.append([1])
            elif i == 1:
                row = [1,1]
                stack.append(row)
            else:
                row = [1] * (i + 1)
                prev = stack[-1]
                for j in range(1, len(row) - 1):
                    row[j] = prev[j] + prev[j - 1]
                stack.append(row)
        return stack.pop()


        