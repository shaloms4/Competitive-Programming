# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                _sum = nums[i] + nums[p1] + nums[p2]
                if _sum == target:
                    return _sum
                if _sum < target:
                    p1 += 1
                else:
                    p2 -= 1
                if abs(target - _sum) < abs(target - closest):
                    closest = _sum
        return closest
