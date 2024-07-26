n, k = map(int, input().split())
sequence = list(map(int, input().split()))

def find_valid_x(n, k, sequence):
    sorted_sequence = sorted(sequence)
    if 0 < k <= n and (k == n or sorted_sequence[k] > sorted_sequence[k - 1]):
        return sorted_sequence[k - 1]
    return -1

print(find_valid_x(n, k, sequence))
