class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        s_ptr = 0
        spaces_ptr = 0
        n = len(s)
        m = len(spaces)
        while s_ptr < n:
            if spaces_ptr < m and s_ptr == spaces[spaces_ptr]:
                result.append(' ')
                spaces_ptr += 1
            result.append(s[s_ptr])
            s_ptr += 1
        return ''.join(result)
        