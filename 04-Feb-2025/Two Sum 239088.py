# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_index:
                return [num_index[diff], i]
            else:
                num_index[nums[i]] = i

        
        