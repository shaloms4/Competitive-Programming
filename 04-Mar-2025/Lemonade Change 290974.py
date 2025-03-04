# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = Counter()
        for i in range(len(bills)):
            if bills[i] == 5:
                count[5] += 1
            elif bills[i] == 10:
                if count[5] < 1:
                    return False
                count[5] -= 1
                count[10] += 1
            elif bills[i] == 20:
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False 
        return True
                    
        