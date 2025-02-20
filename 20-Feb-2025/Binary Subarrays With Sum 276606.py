# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix.append(summ)

        count = 0
        count_sum = defaultdict(int)
        count_sum[0] += 1

        for i in range(len(prefix)):
            diff = prefix[i] - goal
            count += count_sum[diff]
            count_sum[prefix[i]] += 1

        return count 
