class Solution:
    def applyOperations(self, nums):
        i = 0
        n = len(nums)
        
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1
        
        non_zero_index = 0
        
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1
        
        while non_zero_index < n:
            nums[non_zero_index] = 0
            non_zero_index += 1
        
        return nums
