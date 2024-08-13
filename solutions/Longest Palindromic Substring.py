class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
    
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        
        for i in range(len(s)):
            palindrome1 = expand_around_center(i, i)
            palindrome2 = expand_around_center(i, i + 1)
            longest = max(longest, palindrome1, palindrome2, key=len)
        
        return longest
            