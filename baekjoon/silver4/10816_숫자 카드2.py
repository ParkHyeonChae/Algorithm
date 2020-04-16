# 10816_숫자 카드2.py

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
hashmap = {}
result = []

for i in n_list:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for i in m_list:
    if i in hashmap:
        result.append(hashmap[i])
    else:
        result.append(0)

for i in result:
    print(i, end=' ')
        