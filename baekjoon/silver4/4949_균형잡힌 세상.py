# 4949_균형잡힌 세상.py

import sys
input = sys.stdin.readline

s = int(input())
n = 0
plus = 1
s_sum = 0
while s >= s_sum:
    s_sum += plus
    n += 1
    plus += 1

print(n-1)