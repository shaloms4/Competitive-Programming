# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

def min_kicks(s):
    a_score = b_score = 0
    a_remain = b_remain = 5
    res_a = 10

    for i in range(10):
        ch = s[i]
        if i % 2 == 0: 
            if ch == '1' or ch == '?':
                a_score += 1
            a_remain -= 1
        else:  
            if ch == '1':
                b_score += 1
            b_remain -= 1

        if a_score > b_score + b_remain:
            res_a = i + 1
            break
        if b_score > a_score + a_remain:
            res_a = i + 1
            break

    a_score = b_score = 0
    a_remain = b_remain = 5
    res_b = 10

    for i in range(10):
        ch = s[i]
        if i % 2 == 0: 
            if ch == '1':
                a_score += 1
            a_remain -= 1
        else:  
            if ch == '1' or ch == '?':
                b_score += 1
            b_remain -= 1

        if a_score > b_score + b_remain:
            res_b = i + 1
            break
        if b_score > a_score + a_remain:
            res_b = i + 1
            break

    return min(res_a, res_b)

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_kicks(s))
