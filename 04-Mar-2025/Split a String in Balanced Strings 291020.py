# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_num = 0
        balanced = 0
        for char in s:
            if char == "R":
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                max_num += 1
        return max_num