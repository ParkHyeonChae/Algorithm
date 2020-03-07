t = int(input())
arr = []

for i in range(t):
    a, b = map(int, input().split())
    if a > 0 and b < 10:
        arr.append(a+b)

for i in range(t):
    print(arr[i])