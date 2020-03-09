n = input()

n_list = []

for i in range(len(n)):
    n_list.append(n[i])

n_list.sort(reverse=True)

for i in range(len(n)):
    print(n_list[i], end='')