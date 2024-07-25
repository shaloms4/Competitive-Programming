class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        result = []
        size = len(nums)

        for num in range(size):
            if nums[num] == target:
                result.append(num)
        return result