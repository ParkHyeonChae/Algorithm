a, x = map(int, input().split())
arr= list(map(int, input().split()))

for i in range(a):
    if arr[i] < x:
        print(arr[i], end=' ')