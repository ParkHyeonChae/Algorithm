# 2108_통계학.py

import sys
from collections import Counter
input = sys.stdin.readline

n_list = []
n = int(input())
for i in range(n):
    a = int(input())
    n_list.append(a)

def avg():
    n_sum = 0
    for i in range(n):
        n_sum += n_list[i]
    return round(n_sum/n)

def mid():
    n_list.sort()
    return n_list[len(n_list) // 2]

def mode():
    mode_dict = Counter(n_list)
    modes = mode_dict.most_common()
    if len(n_list) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    
    return mod

def range_n():
    max_n = max(n_list)
    min_n = min(n_list)
    return max_n - min_n

print(avg())
print(mid())
print(mode())
print(range_n())