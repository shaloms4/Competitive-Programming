# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

def oi():
  return int(input())
def ostr():
  return input().strip()
t = oi()
for _ in range(t):
    s = ostr()
    t = ostr()
    p = ostr()
    iter_t = iter(t)
    check = all(char in iter_t for char in s)
    if not check:
       print("NO")
       continue
    for char in set(t):
        if s.count(char) + p.count(char) < t.count(char):
            print("NO")
            break  
    else:  
        print("YES") 