# 2609_최대공약수와 최소공배수.py

import sys
input = sys.stdin.readline

n1_list = []
n2_list = []
n1, n2 = map(int, input().split())

for i in range(1, min(n1, n2)+1):
    if n1 % i == 0:
        n1_list.append(i)
    if n2 % i == 0:
        n2_list.append(i)

max_n = max(set(n1_list)&set(n2_list))
min_n = (n1 // max_n) * (n2 // max_n) * max_n

print(max_n)
print(min_n)