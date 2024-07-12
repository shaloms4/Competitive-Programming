class Solution(object):
    def combine(self, n, k):
        combs = []
        subs = []
        def backtrack(i,subs,combs,k,n):
            if len(subs) == k:
                combs.append (subs[:])
                return
            if i > n:
                return
            subs.append(i)
            backtrack(i+1,subs, combs,k,n)
            subs.pop()

            backtrack(i+1,subs, combs,k,n)
        backtrack(1,subs, combs, k,n)
        return combs