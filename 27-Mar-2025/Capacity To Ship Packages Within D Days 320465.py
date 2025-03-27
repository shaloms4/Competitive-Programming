# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(mid):
            k = 0
            weight_sum = 0
            for weight in weights:
                weight_sum += weight
                if weight_sum > mid:
                    k += 1
                    weight_sum = weight
            if weight_sum >= weight:
                k += 1
            
            if k > days:
                return False
            else:
                return True

        low = max(weights)
        high = sum(weights)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if is_valid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans