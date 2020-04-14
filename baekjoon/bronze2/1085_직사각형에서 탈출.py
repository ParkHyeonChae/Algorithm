# 1085_직사각형에서 탈출.py

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min(min(x, w-x), min(y, h-y)))