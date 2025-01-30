# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_word=strs[0]
        last_word=strs[-1]
        n=min(len(first_word),len(last_word))
        for i in range(n):
            if first_word[i]!=last_word[i]:
                return first_word[:i]
        else:
            return first_word