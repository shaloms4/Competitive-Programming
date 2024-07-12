class Solution:
    def subsets(self, nums):
        subs = []
        combs = []
        
        def backtrack(i, combs, subs, nums):
            if i == len(nums):
                subs.append(combs[:])  
                return
            
            combs.append(nums[i])
            backtrack(i+1, combs, subs, nums)
            combs.pop()
            backtrack(i+1, combs, subs, nums)
        
        backtrack(0, combs, subs, nums)
        return subs
