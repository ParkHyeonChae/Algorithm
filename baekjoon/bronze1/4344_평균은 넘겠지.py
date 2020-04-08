# 4344_평균은 넘겠지

import sys
input = sys.stdin.readline

c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0]
    count = 0
    for j in n[1:]:
        if j > avg:
            count += 1
    result = (count / n[0]) * 100
    print(str('%.3f' % round(result, 3))+'%')