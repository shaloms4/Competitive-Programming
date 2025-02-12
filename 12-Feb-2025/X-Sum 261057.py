# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict

t = int(input())
res = []
for i in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    dict_1 = defaultdict(int)
    dict_2 = defaultdict(int)
    for i in range(n):
        for j in range(m):
            dict_1[i-j] += matrix[i][j]
            dict_2[i + j] += matrix[i][j]
    for i in range(n):
        for j in range(m):
            attack_sum = dict_1[i-j] + dict_2[i + j] - matrix[i][j]
            max_sum = max(max_sum, attack_sum)
    res.append(str(max_sum))
print("\n".join(res) + "\n")