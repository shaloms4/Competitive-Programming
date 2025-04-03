# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []
        
        for i in range(len(bucket) - 1, -1, -1):
            while len(ans) < k and bucket[i] != []:
                popped = bucket[i].pop()
                ans.append(popped)
        return ans

            
        