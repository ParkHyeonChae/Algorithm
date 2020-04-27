# 2292_벌집.py

import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
tmp = 6
result = 1
if n== 1:
    print(1)
else:
    while True:
        cnt = cnt + tmp
        result+= 1
        if n <= cnt:
            print(result)
            break
        tmp += 6