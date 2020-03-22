import sys
input = sys.stdin.readline

n = int(input())
ans = [0, 1]

if n == 0:
    print('0')
elif n == 1:
    print('1')
else:
    for i in range(2, n+1):
        ans.append(ans[i-2] + ans[i-1])
    print(ans.pop())

