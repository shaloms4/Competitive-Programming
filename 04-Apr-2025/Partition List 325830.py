# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great_dummy = ListNode()
        less_dummy = ListNode()
        great = great_dummy
        less = less_dummy
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                great.next = head
                great = great.next
            head = head.next
        less.next = great_dummy.next
        great.next = None
        return less_dummy.next



        