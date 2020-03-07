A, B = map(int, input().split())

if A >= -10000 and B <= 10000:
    if A > B :
        print('>')
    elif A < B :
        print('<')
    else :
        print('==') 