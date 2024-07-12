#using Selection Sort
class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if heights[min_idx] < heights[j]:
                    min_idx = j
            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            names[i], names[min_idx] = names[min_idx], names[i]
        return names