# 1094_막대기.py

import sys
input = sys.stdin.readline

x = int(input())
print(str(bin(x)).count('1'))