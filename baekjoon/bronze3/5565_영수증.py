# 5565_영수증.py

import sys
input = sys.stdin.readline

total = 0
n = int(input())
for i in range(9):
    price = int(input())
    total += price

print(n-total)