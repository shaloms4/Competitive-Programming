# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_s = Counter(s)
        checker = count_s[s[0]]
        for key, value in count_s.items():
            if value != checker:
                return False
        return True
        