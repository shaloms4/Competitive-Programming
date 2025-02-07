# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        group, rem = divmod(time, n - 1)

        if group % 2:
            return n - rem
        return rem + 1
        