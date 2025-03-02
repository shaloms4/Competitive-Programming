# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

summ = 0
diag = 0
sec = 0
col = 0
row = 0

for i in range(n):
    diag += mat[i][i]  
    sec += mat[i][n - i - 1] 
    row += mat[n // 2][i]  
    col += mat[i][n // 2]

summ = diag + sec + row + col - 3 * mat[n // 2][n // 2]

print(summ)
