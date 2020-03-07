t = int(input())
result = []
a_list = []
b_list = []

for i in range(1, t+1):
    a, b = map(int, input().split())
    if a > 0 and b < 10:
        a_list.append(a)
        b_list.append(b)
        result.append(a+b)
    
for i in range(1, t+1):
    print('Case #%d: %d + %d = %d' %(i, a_list[i-1], b_list[i-1], result[i-1]))