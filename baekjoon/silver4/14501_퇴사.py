# 14501_퇴사

import sys
input = sys.stdin.readline

n = int(input())
T, P = [], []
dp = [0]*20

for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(n):
    if dp[i+1] < dp[i]:
        dp[i+1] = dp[i]
    if dp[i + T[i]] < dp[i] + P[i]:
        dp[i + T[i]] = dp[i] + P[i]

print(dp[n])