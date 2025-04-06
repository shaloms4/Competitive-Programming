# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

def find_max_population_year(n, people):
    population_changes = defaultdict(int)
    
    for b, d in people:
        population_changes[b] += 1   
        population_changes[d] -= 1   
    
    current_population = 0
    max_population = 0
    best_year = 0  
    for year in sorted(population_changes.keys()):
        current_population += population_changes[year]
        if current_population > max_population:
            max_population = current_population
            best_year = year
    
    return best_year, max_population

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

year, population = find_max_population_year(n, people)
print(year, population)
