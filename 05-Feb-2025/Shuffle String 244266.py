# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [0] * len(indices)
        i = 0
        for num in indices:
            output[num] = s[i]
            i += 1
        return ''.join(output)
        