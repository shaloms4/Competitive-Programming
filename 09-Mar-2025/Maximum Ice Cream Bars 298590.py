# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if min(costs) > coins:
            return 0

        maxi = max(costs)
        count = [0] * (maxi + 1)
        for num in costs:
            count[num] += 1
            
        target = 0
        for idx, num in enumerate(count):
            for j in range(num):
                costs[target] = idx
                target += 1
        
        total = 0
        max_ice = 0
        i = 0
        while i < len(costs) and total + costs[i] <= coins:
            total += costs[i]
            i += 1
            max_ice += 1
        return max_ice

               