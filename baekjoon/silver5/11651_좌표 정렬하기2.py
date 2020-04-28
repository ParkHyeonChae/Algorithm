# 11651_좌표 정렬하기2.py
# 정렬

import sys
input = sys.stdin.readline

n = int(input())
t = []
for i in range(n):
    x, y = map(int, input().split())
    t.append((x, y))

t.sort()
t.sort(key=lambda x : int(x[1]))

for i in range(n):
    print(t[i][0], t[i][1])