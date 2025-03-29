# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = Counter(nums)
    total = float("inf")
    keys = []
    for i in count:
        keys.append(count[i])
    keys.sort()
    for j in range(len(keys)):
        total = min(total, n - keys[j]*(len(keys) - j))
    print(total)