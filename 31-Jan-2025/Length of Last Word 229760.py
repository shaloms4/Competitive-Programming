# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        splitted = s.split(" ")
        for char in splitted:
            if char != "":
                words.append(char)
        return len(words[-1])
        