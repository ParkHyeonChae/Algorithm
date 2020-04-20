# 1547_공.py
# 구현

import sys
input = sys.stdin.readline

m = int(input())
q = [1,2,3]
for _ in range(m):
    x, y = map(int, input().split())
    xi = q.index(x) # 인덱스로 x 위치 담고
    yi = q.index(y) # 인덱스로 y 위치 담고
    q[xi], q[yi] = q[yi], q[xi] # 위치교환, 다른 행으로 교환받으면 error
print(q[0])