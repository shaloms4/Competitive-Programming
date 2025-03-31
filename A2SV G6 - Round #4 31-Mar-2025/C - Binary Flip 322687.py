# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

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
    n = oi()
    nums1 = ostr()
    nums2 = ostr()
    
    def check(nums1, nums2):  
        nums1 += '0'
        nums2 += '0'  
        count = 0

        for i in range(n):
            if nums1[i] == '1':
                count += 1
            else:
                count -= 1
            
            if count != 0:
                if nums1[i] != nums2[i] and nums1[i+1] == nums2[i+1]:
                    print("NO")
                    return           
                elif nums1[i] == nums2[i] and nums1[i+1] != nums2[i+1]:
                    print("NO")
                    return
        
        print("YES")
    check(nums1, nums2)
