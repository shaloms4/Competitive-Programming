# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        mini = abs(min(nums))
        count = [0] * (maxi + mini + 1)
        
        for num in nums:
            count[num + mini] += 1
        target = 0
        for i, num in enumerate(count):
            for j in range(num):
                nums[target] = i - mini
                target += 1
        return nums 
        