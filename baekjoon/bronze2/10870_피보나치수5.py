n = int(input())
num = []

def fibonacci(value):
    if value == 0:
        num.append(0)
    elif value == 1:
        num.append(1)
    num.append(num[value-2]+num[value-1])

    return fibonacci(n-1)

fibonacci(n)
print(num)