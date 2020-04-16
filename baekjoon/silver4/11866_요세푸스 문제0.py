# 11866_요세푸스 문제0.py

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()

for i in range(n):
    q.append(i+1)

print('<', end='')
while q:
    for i in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
print('>', end='')