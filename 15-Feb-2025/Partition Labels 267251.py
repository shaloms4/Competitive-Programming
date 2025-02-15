# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}
        
        partition_sizes = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            
            if i == end:
                partition_sizes.append(end - start + 1)
                start = end + 1
        
        return partition_sizes