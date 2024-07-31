n = int(input())
talents = list(map(int, input().split()))

singers = []
dancers = []
actors = []

for i in range(n):
    if talents[i] == 1:
        singers.append(i + 1)  
    elif talents[i] == 2:
        dancers.append(i + 1) 
    elif talents[i] == 3:
        actors.append(i + 1) 

max_teams = min(len(singers), len(dancers), len(actors))

print(max_teams)

for j in range(max_teams):
    print(singers.pop(0), dancers.pop(0), actors.pop(0))


