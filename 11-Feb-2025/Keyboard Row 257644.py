# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        output = []
        for word in words:
            for i in range(len(word)):
                if word[0].lower() in row1:
                    if word[i].lower() not in row1:
                        break
                elif word[0].lower() in row2:
                    if word[i].lower() not in row2:
                        break
                elif word[0].lower() in row3:
                    if word[i].lower() not in row3:
                        break
            else:
                output.append(word)
        return output

            



                     

                

        