# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars
        def canRepairInTime(time):
            total_cars = 0
            for r in ranks:
                total_cars += int(sqrt(time // r))
                if total_cars >= cars:
                    return True  
            return False

        while left <= right: 
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid - 1  
            else:
                left = mid + 1  
    
        return left  
        