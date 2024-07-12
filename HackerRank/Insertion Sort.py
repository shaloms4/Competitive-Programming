import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    value_to_insert = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value_to_insert:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1
    arr[i + 1] = value_to_insert
    print(" ".join(map(str, arr)))
n = int(input().strip())
arr = list(map(int, input().split()))
insertionSort1(n, arr)



