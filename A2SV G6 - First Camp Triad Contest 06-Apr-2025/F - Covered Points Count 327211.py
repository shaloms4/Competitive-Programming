# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

def covered_points_count(n, segments):
    coords = set()

    for l, r in segments:
        coords.add(l)
        coords.add(r + 1)

    sorted_coords = sorted(coords)
    coord_to_index = {coord: i for i, coord in enumerate(sorted_coords)}

    diff = [0] * (len(sorted_coords) + 1)

    for l, r in segments:
        diff[coord_to_index[l]] += 1
        diff[coord_to_index[r + 1]] -= 1

    result = [0] * (n + 1)
    current = 0

    for i in range(len(sorted_coords) - 1):
        current += diff[i]
        length = sorted_coords[i + 1] - sorted_coords[i]
        if current > 0:
            result[current] += length

    return result[1:]  

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ans = covered_points_count(n, segments)
print(' '.join(map(str, ans)))
