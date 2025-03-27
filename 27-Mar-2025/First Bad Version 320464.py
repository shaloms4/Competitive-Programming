# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        bad_num = 0
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                bad_num = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return bad_num
        