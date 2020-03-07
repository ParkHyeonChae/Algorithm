n = int(input())
x_list = []
y_list = []
rank = 1
result = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(n):
    for j in range(n):
        if x_list[i] < x_list[j]:
            if y_list[i] < y_list[j]:
                rank += 1

    result.append(rank)
    rank = 1

for i in range(n):
    print(result[i])