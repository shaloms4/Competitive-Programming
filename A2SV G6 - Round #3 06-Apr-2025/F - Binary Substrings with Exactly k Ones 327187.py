# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict

k = int(input())
s = input().strip()

prefix_sum = 0
count = 0
freq = defaultdict(int)
freq[0] = 1  

for char in s:
    prefix_sum += int(char)
    count += freq[prefix_sum - k]
    freq[prefix_sum] += 1

print(count)

