# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        output = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                output.append("G")
                i += 1
            elif command[i:i+2] == "()":
                output.append("o")
                i += 2
            else:
                output.append("al")
                i += 4
        return ''.join(output)
            

        