# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        counter = defaultdict(int)
        counter[0] += 1

        count = 0
        for pre in prefix:
            rem = pre % k
            count += counter[rem]
            counter[rem] += 1

        return count
                