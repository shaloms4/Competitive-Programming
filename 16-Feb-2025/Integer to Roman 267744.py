# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        map = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], 
        ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], 
        ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        result = ''
        for symbol, value in map:
            if num // value != 0:
                count = num // value
                result += (symbol * count)
                num = num % value
        return result            



        