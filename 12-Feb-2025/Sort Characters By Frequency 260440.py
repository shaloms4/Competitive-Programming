# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        count_s = Counter(s)
        sort_s = sorted(count_s, key = count_s.get, reverse = True)
        for char in sort_s:
            result.append(char * count_s[char])
        return ''.join(result)
                 
        



        