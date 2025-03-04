# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        j = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= j:
                j = i
        if j == 0:
            return True
        return False   

        


        