# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiple_count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                multiple = nums[i] * nums[j]
                multiple_count[multiple] += 1
        result = 0
        for count in multiple_count.values():
            pairs = (count * (count - 1)) // 2
            result += 8 * pairs
        return result


            
        