# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_splited = path.split('/')
        for path in path_splited:
            if path == "..":
                if stack:
                    stack.pop()
            else:
                if path != "" and path != ".":
                    stack.append(path)
        return "/" + "/".join(stack)
        