import sys

result = []
t = int(input())

if t <= 1000000:
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if a >= 1 and a <= 1000 and b >= 1 and b <= 1000:
            result.append(a+b)

    for i in range(t):
        print(result[i])