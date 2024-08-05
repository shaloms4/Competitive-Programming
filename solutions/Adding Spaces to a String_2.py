class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces_set = set(spaces)
        for i, char in enumerate(s):
            if i in spaces_set:
                result.append(' ')
            result.append(char)
        return ''.join(result)
        