# 2908_상수.py

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

reverse_a = (a // 100) + (a % 10) * 100 + ((a % 100) - (a % 10))
reverse_b = (b // 100) + (b % 10) * 100 + ((b % 100) - (b % 10))

print(max(reverse_a, reverse_b))