# 1978_소수 찾기.py

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
count = n

for i in range(n):   
    if n_list[i] != 1:
        for j in range(n_list[i]-1, 1, -1):
            if n_list[i] % j == 0:
                count -= 1
                break
    else:
        count -= 1
        
print(count)