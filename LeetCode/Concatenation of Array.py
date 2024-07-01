class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

param_1=[1,2,1]
result=Solution().getConcatenation(param_1)
print(result)

