# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact_n = math.factorial(n)

        def count_zeros(number):
            if number % 10 != 0:
                return 0
            return 1 + count_zeros(number // 10)

        ans = count_zeros(fact_n)
        return ans
            
        