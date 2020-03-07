n = int(input())
n_list = list(map(int, input().split()))

min_num = min(n_list)
max_num = max(n_list)

print('%d %d' %(min_num, max_num))