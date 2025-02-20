# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict

n, k, q = list(map(int, input().split()))
res = [0] * (200000 + 2)
res_prefix = []

for _ in range(n):
    l, r = list(map(int, input().split()))
    res[l] += 1
    res[r + 1] += -1
run_sum = 0
for i in range(len(res)):
    run_sum += res[i]
    res_prefix.append(run_sum)
binary = []

for i in range(len(res)):
    if res_prefix[i] < k:
        binary.append(0)
    else:
        binary.append(1)
summ = 0
binary_prefix = []
for i in range(len(res)):
    summ += binary[i]
    binary_prefix.append(summ)

for i in range(q):
    a, b = list(map(int, input().split()))
    print(binary_prefix[b] - binary_prefix[a - 1])
