# 1181_단어 정렬.py

import sys
input = sys.stdin.readline

word = []
result = []

n = int(input())
for i in range(n):
    word.append(input())
set_word = set(word)

for i in set_word:
    result.append((len(i), i))
result.sort()

for len_i, i in result:
    print(i, end='')