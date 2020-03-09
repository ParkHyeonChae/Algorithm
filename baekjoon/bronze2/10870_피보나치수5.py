# n = int(input())

# def fibonacci(value):
#     result = 0
#     n1 = 1
#     n2 = 1
#     # last = 1
#     for i in range(1, value+1):
#         if i == 1:
#             result = 1
#         elif i == 2:
#             result = 1
#         else:
#             # last = result
#             result = n1 + n2
#             n1 = n2
#             n2 = result

#     return result

# print(fibonacci(n))

n = int(input())

def f (n):
    if n < 3:
        return 1
    else:
        return f(n-1) + f(n-2)
    
print(f(n))