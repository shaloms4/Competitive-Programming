# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = [i+1 for i in range(n)]
        curr = 0
        while len(result) > 1:
            curr = (curr + k - 1) % len(result)
            result.pop(curr)
        return result[0]

        
        