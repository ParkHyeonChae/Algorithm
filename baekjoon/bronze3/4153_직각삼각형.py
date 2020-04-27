# 4153_직각삼각형.py
# 구현

import sys
input = sys.stdin.readline

while True:
    n1, n2, n3 = map(int, input().split())
    if n1 == 0 and n2 == 0 and n3 == 0:
        break
    else:
        if n1**2 + n2**2 == n3**2:
            print('right')
        elif n1**2 + n3**2 == n2**2:
            print('right')
        elif n2**2 + n3**2 == n1**2:
            print('right')
        else:
            print('wrong')
