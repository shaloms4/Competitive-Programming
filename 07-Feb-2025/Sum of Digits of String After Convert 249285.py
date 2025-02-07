# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char_list = []
        for char in s:
            char_list.append(str(ord(char) - 96))
        joined_list = ''.join(char_list)
        
        i = 0
        while i < k:
            output = 0
            for num in joined_list:
                output += int(num)
            joined_list = str(output)
            i += 1
        return output
        
        