class Solution(object):
    def targetIndices(self, nums, target):
        maximum = max(nums)
        count = [0] * (maximum + 1)
        
        for num in nums:
            count[num] += 1
        
        target_idx = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[target_idx] = index
                target_idx += 1
        
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result
