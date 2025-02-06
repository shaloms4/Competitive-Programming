# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        count_nums = Counter(nums)
        for key, value in count_nums.items():
            if value == 2:
                output.append(key)
        return output
        