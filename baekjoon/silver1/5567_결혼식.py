# 5567_결혼식.py
# 구현

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
r, f, f2 = [], [], []

for i in range(m):  # 친구관계 튜플로 저장
    a, b = map(int, input().split())
    r.append((a, b))

for i in range(m):  # 1이랑 친구 따로 저장
    if r[i][0] == 1:
        f.append(r[i][1])
    elif r[i][1] == 1:
        f.append(r[i][0])

for i in range(m):  # 1의 친구의 친구 따로 저장
    if r[i][0] in f:
        f2.append(r[i][1])
    elif r[i][1] in f:
        f2.append(r[i][0])
        
print(len(set(f+f2))-1) # 각 리스트 합치고 중복제거