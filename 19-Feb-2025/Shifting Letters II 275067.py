# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_amounts = [0] * (n + 1)
        
        for start, end, direction in shifts:
            if direction == 1:  
                shift_amounts[start] += 1
                shift_amounts[end + 1] -= 1
            else:  
                shift_amounts[start] -= 1
                shift_amounts[end + 1] += 1
        current_shift = 0
        s = list(s)
        for i in range(n):
            current_shift += shift_amounts[i]
            s[i] = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
        
        return ''.join(s) 
