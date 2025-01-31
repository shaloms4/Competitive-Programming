# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for i in range(len(s)):
            if s[i].isalnum() and s[i] != " ":
                output.append(s[i].lower())
        joined = ''.join(output)
        if joined == joined[::-1]:
            return True
        return False

