t = int(input())
result = []

for i in range(1, t+1):
    a, b = map(int, input().split())
    if a > 0 and b < 10:
        result.append(a+b)
    
for i in range(1, t+1):
    print('Case #%d: %d' %(i, result[i-1]))
