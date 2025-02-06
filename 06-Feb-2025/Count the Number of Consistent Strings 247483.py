# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count_allowed = Counter(allowed)
        count = 0
        for word in words:
            for char in word:
                if char not in count_allowed:
                    break
            else:
                count += 1
        return count
        