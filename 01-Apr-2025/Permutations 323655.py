# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(res, nums, ans):
            if len(res) == len(nums):
                ans.append(res[:])  
                return
            for i in range(len(nums)):
                if nums[i] in res:
                    continue
                res.append(nums[i])
                helper(res, nums, ans)
                res.pop()
        
        ans = []
        helper([], nums, ans)
        return ans
        