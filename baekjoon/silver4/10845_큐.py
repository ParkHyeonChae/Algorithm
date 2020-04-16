# 10845_큐.py

import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        q.append(cmd[1])
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
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        if q:
            print(q[0])
            del q[0]
        else:
            print(-1)