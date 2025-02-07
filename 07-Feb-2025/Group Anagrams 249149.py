# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        result = []

        for s in strs:
            sorted_strs = tuple(sorted(s))
            anagram_dict[sorted_strs].append(s)
        for value in anagram_dict.values():
            result.append(value)
        return result
        