if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    max_score = max(A)
    while max_score in A:
        A.remove(max_score)
    runner_up_score = max(A)
    print(runner_up_score)
