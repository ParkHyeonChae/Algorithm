# 1065_한수

import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(1, n+1):
    if len(str(i)) <= 2:
        count += 1
    else:
        if int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1]):
            count += 1

print(count)