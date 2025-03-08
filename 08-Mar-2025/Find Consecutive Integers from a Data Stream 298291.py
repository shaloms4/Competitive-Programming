# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.queue = deque()
        
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1

        while len(self.queue) > self.k:
            popped = self.queue.popleft()
            if popped == self.value:
                self.count -= 1
        if self.count == self.k:
            return True 
        return False

