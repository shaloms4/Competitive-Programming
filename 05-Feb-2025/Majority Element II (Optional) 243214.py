# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        output = []
        for key, value in count_nums.items():
            if value > len(nums) / 3:
                output.append(key)
        return output

        