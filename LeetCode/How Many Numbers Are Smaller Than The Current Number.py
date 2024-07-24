class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        count = [0] * n
        for i in range(n):
            for j in range(n):
                if j != i and nums[j] < nums[i]:
                    count[i] += 1
        return count 
