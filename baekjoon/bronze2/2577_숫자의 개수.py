# 2577_숫자의 개수

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = a * b * c
count = 0

for i in range(0, 10):
    for j in range(len(str(result))):
        if str(result)[j] == str(i):
            count += 1
    print(count)
    count = 0