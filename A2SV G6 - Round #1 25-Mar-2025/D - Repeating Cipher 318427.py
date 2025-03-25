# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

def oi():
  return int(input())
def ostr():
  return input().strip()
n = oi()
s = ostr()
i = 0
j = 1
res = []
while i < n:
    res.append(s[i])
    i += j
    j += 1
print(''.join(res))
    