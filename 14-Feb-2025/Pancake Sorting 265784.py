# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        n = len(arr)

        for max_num in range(n, 0, -1):  
            idx = arr.index(max_num)  
            if idx == max_num - 1:
                continue  
            if idx != 0:
                arr[:idx + 1] = reversed(arr[:idx + 1])
                output.append(idx + 1)
            arr[:max_num] = reversed(arr[:max_num])
            output.append(max_num)

        return output
