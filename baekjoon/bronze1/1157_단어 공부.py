# 1157_단어 공부.py

import sys
input = sys.stdin.readline

arr = [0]*26
max_alp = 0
s = list(input().upper())

for i in range(len(s)):
    for j in range(26):
        if ord(s[i]) == j+65:
            arr[j] += 1

if arr.count(max(arr)) >= 2:
    print("?")
else:
    print(chr(arr.index(max(arr))+65))