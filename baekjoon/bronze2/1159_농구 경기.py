# 1159_농구 경기.py
# 구현

import sys
input = sys.stdin.readline

m = []
n = int(input())
for i in range(n):
    m.append(input())

r = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if m[i][0] == m[j][0]:
            cnt += 1
        if cnt >= 5:
            r.append(m[i][0])

if set(r):
    for i in sorted(set(r)):
        print(i, end='')
else:
    print('PREDAJA')