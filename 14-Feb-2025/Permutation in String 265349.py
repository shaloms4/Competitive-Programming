# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        cur_s2 = Counter(s2[:len(s1) - 1])
        for right in range(len(s1) - 1, len(s2)):
            cur_s2[s2[right]] += 1
            if cur_s2 == Counter(s1):
                return True
            cur_s2[s2[right - len(s1) + 1]] -= 1
            if cur_s2[s2[right - len(s1) + 1]] == 0:
                del cur_s2[s2[right - len(s1) + 1]]
        return False



        