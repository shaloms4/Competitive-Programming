# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False  
        new_source = [] 
        current_line = "" 

        for line in source:
            i = 0
            if not in_block:
                current_line = ""  

            while i < len(line):
                if not in_block and line[i:i+2] == "/*":
                    in_block = True
                    i += 1  
                elif in_block and line[i:i+2] == "*/":
                    in_block = False
                    i += 1 
                elif not in_block and line[i:i+2] == "//":
                    break  
                elif not in_block:
                    current_line += line[i] 
                i += 1
            if not in_block:
                new_source.append(current_line) 
        
        return [line for line in new_source if line != ""]
