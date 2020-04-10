# 4641_Doubles.py

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == -1:
        break
    count = 0
    for i in range(len(arr)-1):
        if arr[i]*2 in arr:
            count += 1
    print(count)