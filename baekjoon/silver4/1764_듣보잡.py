# 1764_듣보잡.py
# 구현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

if len(a) >= len(b):
    result = set(a) - (set(a)-set(b))
else:
    result = set(b) - (set(b)-set(a))

print(len(result))
for i in sorted(result):
    print(i[:-1])