# 9012_괄호.py

import sys
input = sys.stdin.readline

result = []
t = int(input())

for i in range(t):
    stack = []
    vps = list(input())
    if vps[0] != ')' and vps.count('(') == vps.count(')'):
        for i in range(len(vps)-1):
            if vps[i] == '(':
                stack.append(vps[i])
            elif stack and vps[i] == ')':
                stack.pop()
        if not stack:
            result.append('YES')
        else:
            result.append('NO')
    else:
        result.append('NO')

for i in range(t):
    print(result[i])