# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def rotate(matrix):
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]

        return rotated

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    mat = []
    for _ in range(n):
        row =  list(input())
        mat.append(row)
    
    min_operations = 0
    rotate_90 = rotate(mat)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            ans = [mat[i][j], rotate_90[i][j], rotate_180[i][j], rotate_270[i][j]]
            count_ones = ans.count('1')
            count_zeros = 4 - count_ones
            min_operations += min(count_zeros, count_ones)

    print(min_operations)
