# Problem: Arithmetic Operators - https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]