# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        num = int(''.join(map(str, digits)))
        num += 1   
        num_str = str(num)
        
        for digit in num_str:
            result.append(int(digit))
            
        return result