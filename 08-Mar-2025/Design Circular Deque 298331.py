# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = deque()
        

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        return False        

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False 
        

    def deleteFront(self) -> bool:
        if not self.queue:
            return False
        self.queue.popleft()
        return True
        

    def deleteLast(self) -> bool:
        if not self.queue:
            return False
        self.queue.pop()
        return True
        

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1
        

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1
        
        
    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True
        

    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        return False
        

