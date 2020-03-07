num_list = []

for i in range(9):
    num_list.append(int(input()))

max_num = max(num_list)
location = num_list.index(max_num)+1

print(max_num)
print(location)