# 2164_카드.py

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
n_list = deque()
for i in range(1, n+1):
    n_list.append(i)

while True:
    if len(n_list) == 1:
        print(n_list[0])
        break
    del n_list[0]
    n_list.append(n_list[0])
    del n_list[0]