# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from typing import Counter


def oi():
  return int(input())
def ti():
  return map(int, input().split())
def ostr():
  return input().strip()
def li():
  return list(map(int, input().split()))
t = oi()
for _ in range(t):
    n, k, d = ti()
    nums = li()
    count = Counter(nums[:d - 1])
    mini = float('inf')
    for i in range(d - 1, n):
        count[nums[i]] += 1
        mini = min(mini, len(count))
        count[nums[i - d + 1]] -= 1
        if count[nums[i - d + 1]] == 0:
            del count[nums[i - d + 1]]
    print(mini)
        
    