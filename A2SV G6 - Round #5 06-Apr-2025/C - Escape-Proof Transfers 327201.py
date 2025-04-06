# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

from typing import Counter


n, crime_level, choose = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
count = 0
for right in range(n):
     
    if nums[right] > crime_level:
        left = right+1
    currlength = right - left + 1
    if currlength >= choose:
        count += 1
print(count)