class Solution(object):
    def binaryTreePaths(self, root):
        arr = []
        s = []
        def backtrack(root, arr, s):
            if root:
                s.append(str(root.val))
                if not root.right and not root.left:
                    arr.append("->".join(s))
                backtrack(root.left,arr,s)
                backtrack(root.right,arr,s)
                s.pop()
        backtrack(root,arr,s)
        return arr