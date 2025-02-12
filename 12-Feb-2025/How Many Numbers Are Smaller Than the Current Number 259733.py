# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count[i] += 1
            
        return count
        

        