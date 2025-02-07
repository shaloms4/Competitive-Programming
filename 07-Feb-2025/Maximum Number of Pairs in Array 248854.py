# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = 0
        leftover = 0
        count_num = Counter(nums)
        for key, value in count_num.items():
            if value % 2 == 0:
                pair += value//2
            else:
                pair += value//2
                leftover += value % 2 
        return [pair, leftover]


        


        