# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i = 0
        while i < n:
            idx = nums[i] - 1
            if nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

        