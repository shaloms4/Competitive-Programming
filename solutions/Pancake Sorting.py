class Solution(object):
    def pancakeSort(self, arr):
        def flip(sub_arr, k):
            sub_arr[:k] = sub_arr[:k][::-1]
        
        def find_max_index(arr, n):
            max_index = 0
            for i in range(n):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index
        
        flips = []
        size = len(arr)
        
        for i in range(size, 1, -1):
            max_index = find_max_index(arr, i)
            
            if max_index + 1 == i:
                continue
            
            if max_index != 0:
                flip(arr, max_index + 1)
                flips.append(max_index + 1)
            
            flip(arr, i)
            flips.append(i)
        
        return flips
