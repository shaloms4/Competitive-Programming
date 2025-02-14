# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        max_num = 0 
        for i in range(1, 2 * len(piles)//3, 2):
            max_num += piles[i]
            
        return max_num 
             

        