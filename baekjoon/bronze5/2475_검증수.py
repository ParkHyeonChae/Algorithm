# 2475_검증수.py

import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
n_sum = 0

for i in range(len(n)):
    n_sum += n[i]**2

print(n_sum % 10)