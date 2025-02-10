# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        max_num = max(nums)
        count = [0] * (max_num + 1)

        for num in nums:
            count[num] += 1

        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1
        return target

        