# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_nums = Counter(nums)
        for key, value in count_nums.items():
            if value > 1:
                return True
        return False
        