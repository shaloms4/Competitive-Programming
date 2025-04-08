# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_decrement = [0] * (n + 1)

        def canMakeZero(k):
            current_decrement = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                current_decrement[l] += val
                if r + 1 < n:
                    current_decrement[r + 1] -= val
            
            for i in range(1, n):
                current_decrement[i] += current_decrement[i - 1]

            for i in range(n):
                if nums[i] - current_decrement[i] > 0:
                    return False
            return True
        
        left, right = 0, len(queries)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
