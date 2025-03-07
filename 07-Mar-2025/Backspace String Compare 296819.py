# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i == '#':
                stack.pop()
            else:
                stack.append(i)

        stack2 = []
        for i in t:
            if i == '#':
                stack.pop()
            else:
                stack.append(i)
        return
        
        
            
        

        