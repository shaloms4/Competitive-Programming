# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {"/", "+", "-", "*"}
        for char in tokens:
            if char in operation:
                b = stack.pop()
                a = stack.pop() 

                if char == "/":
                    stack.append(int(a/b))
                elif char == "+":
                    stack.append(a + b)
                elif char == "-":
                    stack.append(a - b)
                elif char == "*":
                    stack.append(a * b)
            else:
                stack.append(int(char))
        return stack[0]


        