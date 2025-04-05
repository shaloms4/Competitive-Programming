# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            idx = nums[i] - 1
            if nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        