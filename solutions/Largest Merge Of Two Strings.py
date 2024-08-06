class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        pointer_1 = 0
        pointer_2 = 0
        while pointer_1 < len(word1) or pointer_2 < len(word2):
            if word1[pointer_1:] > word2[pointer_2:]:
                merge.append(word1[pointer_1])
                pointer_1 += 1
            else:
                merge.append(word2[pointer_2])
                pointer_2 += 1
        return ''.join(merge)