# 10814_나이순 정렬.py

import sys
input = sys.stdin.readline

member = []
n = int(input())
for i in range(n):
    age, name = map(str, input().split())
    member.append((int(age), name))

member.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(member[i][0], member[i][1])