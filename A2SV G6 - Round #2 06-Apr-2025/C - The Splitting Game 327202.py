# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

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
    n = oi()
    s = ostr()

    right = Counter(s)
    left = Counter()
    maxi = 0
    for char in s:
        left[char] += 1
        right[char] -= 1
        if right[char] == 0:
            del right[char]
        maxi = max(maxi, len(right) + len(left))
    print(maxi)