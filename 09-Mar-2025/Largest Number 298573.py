# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
        str_nums.sort(key=cmp_to_key(compare))
        return ''.join(str_nums) if ''.join(str_nums)[0] != '0' else '0'
        