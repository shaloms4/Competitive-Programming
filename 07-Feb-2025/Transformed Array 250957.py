# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        if len(nums) == 1:
                return nums
        for i in range(len(nums)):
            
            if nums[i] > 0:
                result[i] = nums[(i + nums[i]) % len(nums) ] 
            elif nums[i] < 0: 
                result[i] = nums[(i - abs(nums[i])) % len(nums)] 
            elif nums[i] == 0:
                result[i] = nums[i]
        return result

        