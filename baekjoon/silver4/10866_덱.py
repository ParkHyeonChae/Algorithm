# 10866_덱.py

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push_front':
        q.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        q.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if q:
            print(q[0])
            del q[0]
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if q:
            print(q[-1])
            del q[-1]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)