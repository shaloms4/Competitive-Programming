def find_path_sum(n):
    total_sum = 0
    while n > 0:
        total_sum += n
        n //= 2
    return total_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0]) 
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i]) 
        result = find_path_sum(n)  
        results.append(result) 
    
    for result in results:
        print(result)  

if __name__ == "__main__":
    main()
