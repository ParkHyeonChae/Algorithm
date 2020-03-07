n = int(input())

def factorial(value):
    if value == 0:
        return 1
    elif value == 1:
        return 1
    return value * factorial(value-1)

print(factorial(n))