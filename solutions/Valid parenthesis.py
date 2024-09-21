class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_dict = {'(':')', '{':'}', '[':']'}
        for i in range(len(s)):
            if s[i] in char_dict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                removed = stack.pop()
                if s[i] != char_dict[removed]:
                    return False
        return stack == []


        