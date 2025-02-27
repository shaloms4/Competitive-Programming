# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur = head
        second = cur.next
        index = 0
        prev = None
        while cur.next:
            next_node = cur.next
            cur.next = cur.next.next
            prev = cur
            cur = next_node
            index += 1
        if index % 2 == 0:
            cur.next = second
        else:
            prev.next = second
        return head

        