# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        list_s = list(s)
        left = 0
        count = 0
        for right in range(len(s)):
            if list_s[right] == "0":
                list_s[right], list_s[left] = list_s[left], list_s[right]
                count += right - left
                left += 1
        return count
            


        