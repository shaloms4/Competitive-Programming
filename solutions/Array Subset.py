from collections import Counter

def isSubset(a1, a2, n, m):
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    
    for element in count_a2:
        if count_a2[element] > count_a1.get(element, 0):
            return 'No'
    return 'Yes'
