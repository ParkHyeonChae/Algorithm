A, B, C = map(int, input().split())

if A >= 2 and B >= 2 and C >= 2 and A <= 10000 and B <= 10000 and C <= 10000:
    result1 = (A+B)%C
    result2 = (A%C + B%C)%C
    result3 = (A*B)%C
    result4 = (A%C * B%C)%C

    print(result1)
    print(result2)
    print(result3)
    print(result4)