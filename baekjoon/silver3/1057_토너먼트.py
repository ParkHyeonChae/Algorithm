# 1057_토너먼트.py
# 구현

import sys
input = sys.stdin.readline

num, a, b = map(int, input().split())
count = 0
flag = 1
while num != 1:
    count=count + 1
    num = num / 2
    a = (a + 1) // 2
    b = (b + 1) // 2
    if a == b:
        print(count)
        flag=0
        break

if flag == 1:
    print(-1)