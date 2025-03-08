# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.popleft()
        
    def peek(self) -> int:
        if not self.queue:
            return
        return self.queue[0]
        

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False
        