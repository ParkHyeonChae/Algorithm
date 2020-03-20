import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for i in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for i in stack:
    result += i

print(result)