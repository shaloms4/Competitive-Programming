# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        counter = defaultdict(int)
        counter[0] += 1

        count = 0
        for pre in prefix:
            diff = pre - k
            count += counter[diff]
            counter[pre] += 1
        return count