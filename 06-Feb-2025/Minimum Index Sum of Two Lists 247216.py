# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count_list1 = defaultdict(int)
        count_list2 = defaultdict(int)
        output = []
        min_idx = float('inf')

        for idx, word in enumerate(list1):
            if word in list2:
                count_list1[word] = idx

        for idx, word in enumerate(list2):
            if word in list1:
                count_list2[word] = idx

        for key, value in count_list1.items():
            min_idx = min(min_idx, value + count_list2[key])
            
        for key, value in count_list1.items():
            if value + count_list2[key] == min_idx:
                output.append(key)
        return output
        







        