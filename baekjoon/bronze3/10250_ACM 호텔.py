# 10250_ACM 호텔.py

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    if h == 1:
        print(100 + (n // h))
    else:
        if n % h == 0:
            print(h * 100 + n // h)
        else:
            print((n % h * 100) + (n // h + 1))