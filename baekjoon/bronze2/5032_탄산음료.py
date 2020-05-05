# 5032_탄산음료.py

import sys
input = sys.stdin.readline

e, f, c = map(int, input().split())
s = e + f
result = 0

while s >= c:
    result += s // c
    s = s // c + s % c

print(result)