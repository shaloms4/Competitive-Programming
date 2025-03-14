# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900 }
        count = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in symbol:
                count += symbol[s[i:i + 2]]
                i += 2  
            else:
                count += symbol[s[i]]
                i += 1  
        
        return count