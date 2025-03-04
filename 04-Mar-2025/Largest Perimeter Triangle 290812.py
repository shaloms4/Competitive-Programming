# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        [1,1,2,10]
        p1 = len(nums) - 1
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] + nums[i - 1] > nums[p1]:
                return nums[i] + nums[i - 1] + nums[p1]
            p1 -= 1
        return 0
            


        


        