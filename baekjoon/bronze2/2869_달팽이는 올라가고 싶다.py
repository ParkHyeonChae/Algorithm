# 2869_달팽이는 올라가고 싶다.py

import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())
print(math.ceil((v - a) / (a - b)) + 1)