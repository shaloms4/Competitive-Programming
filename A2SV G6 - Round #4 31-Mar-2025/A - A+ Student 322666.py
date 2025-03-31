# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

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
    res = []
    a,b,c = li()

    res.append(max(0, max(b,c) - a + 1))
    res.append(max(0, max(a,c) - b + 1))
    res.append(max(0, max(a,b) - c + 1))
    print(*res)
    
        