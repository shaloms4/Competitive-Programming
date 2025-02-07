# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = list(s)
        for i in range(len(s_list)):
            popped = s_list.pop()
            s_list.insert(0,popped)
            if ''.join(s_list) == goal:
                return True
        return False
        
        
        