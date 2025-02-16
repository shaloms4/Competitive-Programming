# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        for val, idx in queries:
            old = nums[idx]
            nums[idx] += val
            if old % 2 == 0:
                even_sum -= old
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            res.append(even_sum)
        return res
        