# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0 or n == 2:
            return n
        else:
            return 2 * n

        
        