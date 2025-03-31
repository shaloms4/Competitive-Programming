# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

def oi():
  return int(input())
def ti():
  return map(int, input().split())
def ostr():
  return input().strip()
def li():
  return list(map(int, input().split()))

building, queries = ti()
height = li()

forward = [0] * building
for i in range(1, building):
    if height[i] < height[i - 1]:  
        forward[i] = forward[i - 1] + (height[i - 1] - height[i])
    else:
        forward[i] = forward[i - 1]

backward = [0] * building
for i in range(building - 2, -1, -1):
    if height[i] < height[i + 1]:  
        backward[i] = backward[i + 1] + (height[i + 1] - height[i])
    else:
        backward[i] = backward[i + 1]

for _ in range(queries):
    s, t = ti()
    
    if s < t:
        print(forward[t - 1] - forward[s - 1])
    else:
        print(backward[t - 1] - backward[s - 1])