# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            sum_of_squares = left * left + right * right
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                left += 1
            else:
                right -= 1
        
        return False

