# 5532_방학 숙제.py
# 구현

import sys
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

n1, n2 = 0, 0
if a%c == 0:
    n1 = a//c
else:
    n1 = a//c+1
if b%d == 0:
    n2 = b//d
else:
    n2 = b//d+1

print(l - max(n1, n2))