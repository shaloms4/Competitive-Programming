# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

def oi():
  return int(input())
def li():
    return list(map(int, input().split()))

n = oi()
nums = li()
nums.sort()
if n % 2 == 0:
    print(nums[n//2 - 1])
else:
    print(nums[n//2])