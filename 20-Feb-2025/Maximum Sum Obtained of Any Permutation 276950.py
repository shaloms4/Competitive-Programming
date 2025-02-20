# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
        pre_sum = []
        summ = 0
        for num in prefix:
            summ += num
            pre_sum.append(summ)
        print(pre_sum)
        pre_sum.pop()
        pre_sum.sort()
        nums.sort()
        max_sum = sum([p*n for p,n in zip(pre_sum, nums)]) % (10**9 + 7)
        return max_sum



