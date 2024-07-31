class Solution:
    def check(self, arr1, arr2) -> bool:
        equal_size = set(arr1) == set(arr2)
        return equal_size