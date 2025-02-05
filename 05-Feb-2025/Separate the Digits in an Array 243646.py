# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            for n in str(num):
                output.append(int(n))
        return output


        