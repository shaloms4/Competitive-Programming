# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
 
n, k = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque()
check = set()
for i in range(n):
    if nums[i] not in check:
        queue.appendleft(nums[i])
        check.add(nums[i])
    while len(queue) > k:
        popped = queue.pop()
        check.remove(popped)
print(len(queue))
print(*queue)