# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for nums in accounts:
            account_sum = sum(nums)
            wealth = max(wealth, account_sum)
        return wealth
           
        

        