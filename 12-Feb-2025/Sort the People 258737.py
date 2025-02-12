# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if heights[max_idx] < heights[j]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]
        return names