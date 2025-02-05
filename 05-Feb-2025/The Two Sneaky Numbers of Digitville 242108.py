# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []
        count_nums = Counter(nums)
        for key, value in count_nums.items():
            if value == 2:
                output.append(key)
        return output

        