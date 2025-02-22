# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.count = 0

    def get(self, index: int) -> int:
        if index >=self.count:
            return -1
        else:
            cur_idx = 0
            cur_node = self.dummy.next
            while cur_idx < index:
                cur_node = cur_node.next
                cur_idx += 1
            return cur_node.val

    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        new_node = Node(val)
        self.dummy.next = new_node
        new_node.next = head
        self.count += 1

        if not self.tail:
            self.tail = new_node
        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index == self.count:
            self.addAtTail(val)
        else:
            cur_idx = 0
            cur_node = self.dummy
            while cur_idx < index:
                cur_node = cur_node.next
                cur_idx += 1
            new_node = Node(val)
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.count += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return 
        cur_idx = 0
        cur_node = self.dummy
        while cur_idx < index:
            cur_node = cur_node.next
            cur_idx += 1
        cur_node.next = cur_node.next.next
        
        if not cur_node.next:
            self.tail = cur_node
        self.count -= 1
        
        
