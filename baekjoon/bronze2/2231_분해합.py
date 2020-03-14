n = int(input())
k_sum = 0
result_list = []
min_result = n

for i in range(n):
    k = str(i)
    for i in range(len(k)):
        k_sum += int(k[i])
    result = k_sum + int(k)
    if result == n:
        result_list.append(int(k))
    k_sum = 0

for i in range(len(result_list)):
    min_result = min(min_result, result_list[i])

if not result_list:
    min_result = 0

print(min_result)