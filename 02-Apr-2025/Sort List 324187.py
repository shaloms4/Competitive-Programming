# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        res = []
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next
        res.sort(key= lambda x:x.val)
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        res[-1].next = None

        return res[0]