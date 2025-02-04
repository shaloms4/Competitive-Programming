# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_set = set()
        for i in ranges:
            for num in range(i[0], i[1] + 1):
                ranges_set.add(num)
        for i in range(left, right + 1):
            if i not in ranges_set:
                return False
        return True
        