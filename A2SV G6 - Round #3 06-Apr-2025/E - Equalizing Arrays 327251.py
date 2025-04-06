# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E


n = int(input())
a = list(map(int, input().strip().split()))
m = int(input().strip())
b = list(map(int, input().strip().split()))

if sum(a) != sum(b):
    print(-1)
    exit()

p1 = 0 
p2 = 0

cur_sum1 = 0
cur_sum2 = 0

ans = 0

while p1 < n:
    
    cur_sum1 += a[p1]
    cur_sum2 += b[p2]
    p1 += 1
    p2 += 1

    while cur_sum1 != cur_sum2:
        if cur_sum1 < cur_sum2:
            cur_sum1 += a[p1]
            p1 += 1
        else:
            cur_sum2 += b[p2]
            p2 += 1
    ans += 1
print(ans)