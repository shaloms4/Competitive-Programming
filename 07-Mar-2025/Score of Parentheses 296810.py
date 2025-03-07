# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for par in s:
            if par == '(':
                stack.append(0)
            else:
                inner_score = stack.pop()
                stack[-1] += max(2 * inner_score, 1)
        
        return stack[0]