# Problem: Books - https://codeforces.com/contest/279/problem/B

def oi():
  return int(input())
def ti():
  return map(int, input().split())
def ostr():
  return input().strip()
def li():
  return list(map(int, input().split()))
books, minutes = ti()
nums = li()
maxi = 0
summ = 0
left = 0
for right in range(books):
    summ += nums[right]
    while summ > minutes and left < len(nums):
        summ -= nums[left]
        left += 1
    maxi = max(maxi, right - left + 1)
print(maxi)
        
        
      