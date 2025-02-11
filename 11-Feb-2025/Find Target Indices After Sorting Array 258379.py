# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += 1
        j = 0
        for i, val in enumerate(count):
            for _ in range(val):
                nums[j] = i
                j += 1
        print(nums)
        return [i for i in range(len(nums)) if nums[i] == target]

        
