# 2455_지능형 기차.py

import sys
input = sys.stdin.readline
result = [0]
while True:
    n, m = map(int, input().split())
    result.append(result[-1]-n+m)
    if m == 0:
        break

print(max(result))