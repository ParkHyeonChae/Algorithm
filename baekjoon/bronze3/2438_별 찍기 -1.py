# n = int(input())

# if n >= 1 and n <= 100:
#     for i in range(1, n+1):
#         print()
#         for i in range(i):
#             print('*', end='')

n = int(input())

if n >= 1 and n <= 100:
    for i in range(1, n+1):
        print('*'*i)