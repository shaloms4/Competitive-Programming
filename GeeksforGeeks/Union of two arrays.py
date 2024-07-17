class Solution:    
    def doUnion(self,arr1,arr2):
        union_arr = set(arr1) | set(arr2)
        number_of_elements = len(union_arr)
        return number_of_elements