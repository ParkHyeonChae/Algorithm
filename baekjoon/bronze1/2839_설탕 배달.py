# 2839_설탕 배달.py
# 구현

import sys
input = sys.stdin.readline

n = int(input())
r = 1000 - n
cnt = 0

while True:
    if r == 0:
        break
    if r // 500 > 0:
        cnt += r//500
        r = r - (r // 500 * 500)
    elif r // 100 > 0:
        cnt += r//100
        r = r - (r // 100 * 100)
    elif r // 50 > 0:
        cnt += r//50
        r = r - (r // 50 * 50)
    elif r // 10 > 0:
        cnt += r//10
        r = r - (r // 10 * 10)
    elif r // 5 > 0:
        cnt += r//5
        r = r - (r // 5 * 5)
    elif r // 1 > 0:
        cnt += r//1
        r = r - (r // 1)
        
print (cnt)