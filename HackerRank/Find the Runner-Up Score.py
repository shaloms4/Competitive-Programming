if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    
    highest_score = max(scores)
    
    runner_up = None
    for score in scores:
        if score != highest_score and (runner_up is None or score > runner_up):
            runner_up = score
    
    if runner_up is None:
        print("No runner-up score found.")
    else:
        print(runner_up)
