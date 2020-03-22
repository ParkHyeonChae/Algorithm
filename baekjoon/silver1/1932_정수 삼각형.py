import sys
input = sys.stdin.readline

arr = []
k = 0
ans = 0
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))

arr[1][0] = arr[1][0] + arr[0][0]
arr[1][1] = arr[1][1] + arr[0][0]

for i in range(2, n):
    for j in range(k+3):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == (k+2):
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i][j] + arr[i-1][j-1], arr[i][j] + arr[i-1][j])
    k += 1

for i in range(n):
    num = arr[n-1][i]
    ans = max(ans, num)

print (ans)