from itertools import combinations

n, m = map(int, input().split())
n_list = []

for i in range(1, n+1):
    n_list.append(i)

result = list(combinations(n_list, m))

for i in range(len(result)):
    print(str(result[i])[1:-1].replace(",",""))