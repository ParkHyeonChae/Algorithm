# 1547_공.py

import sys
input = sys.stdin.readline

m = int(input())
q = [1,2,3]
for _ in range(m):
    x, y = map(int, input().split())
    xi = q.index(x)
    yi = q.index(y)
    q[xi], q[yi] = q[yi], q[xi]
print(q[0])