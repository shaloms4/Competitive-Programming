class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        palindrome = str_x[::-1]
        if str_x == palindrome:
            return True
        else:
            return False
