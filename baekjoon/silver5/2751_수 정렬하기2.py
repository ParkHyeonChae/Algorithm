import sys

n_list = []
n = int(sys.stdin.readline())
for i in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

for i in range(n):
    print(n_list[i])