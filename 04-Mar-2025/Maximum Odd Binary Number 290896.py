# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = []
        count = Counter(s)
        if count['1'] != 1:
            res.append('1' * (count['1'] - 1))
        res.append('0' * count['0'])
        res.append('1')
        return ''.join(res)