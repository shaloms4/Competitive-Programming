def can_reduce_to_one_element(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        result = can_reduce_to_one_element(arr)
        results.append(result)
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
