# 11650_좌표 정렬하기.py

import sys
input = sys.stdin.readline

xy = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

xy.sort()
for i in range(n):
    print(xy[i][0], xy[i][1])