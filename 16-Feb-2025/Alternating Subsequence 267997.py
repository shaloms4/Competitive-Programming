# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    t = int(input())
    nums = list(map(int, input().split()))
    res = []
    for i in range(len(nums)):
        if res == []:
            res.append(nums[i])
        if res[-1] > 0:            
            if res[-1] < nums[i]:
                res.pop()
                res.append(nums[i])
            elif nums[i] < 0:
                res.append(nums[i])
        elif res[-1] < 0:
            if nums[i] > 0:
                res.append(nums[i])
            elif nums[i] > res[-1]:
                res.pop()
                res.append(nums[i])
    print(sum(res))
        




