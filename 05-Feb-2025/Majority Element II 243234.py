# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        output = []
        for key, value in count_nums.items():
            if value > len(nums) / 3:
                output.append(key)
        return output

        