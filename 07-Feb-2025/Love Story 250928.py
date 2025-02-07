# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
s = "codeforces"
for i in range(t):
    strs = input()
    count = 0
    for i in range(len(strs)):
        if strs[i] != s[i]:
            count += 1
    print(count)