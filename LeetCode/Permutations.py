class Solution:
    def helper(self, res, nums, ans) :
        if len(nums) == len(res):
            ans.append (res[:])
            return
        for i in range(len(nums)):
            if nums[i] in res:
                continue
            res.append (nums [i])
            self.helper(res, nums, ans)
            res.pop()
    def permute(self, nums):
        ans = []
        self.helper([], nums, ans)
        return ans

      