# 2839_설탕 배달.py

import sys
input = sys.stdin.readline

n = int(input())
result = 0
while n > 0 :
    if n % 5 != 0:
        n -= 3
        if n < 0:
            result = -1
            break
        result += 1
    elif n % 5 == 0:
        result += 1
        n -= 5
    elif n % 5 != 0 and n % 3 != 0:
        result = -1
print(result)