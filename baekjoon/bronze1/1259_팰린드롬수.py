# 1259_팰린드롬수.py

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    if len(str(n)) == 1:
        print("yes")
    elif len(str(n)) == 2:
        if int(str(n)[0]) + int(str(n)[1]) * 10 == n:
            print("yes")
        else:
            print("no")
    elif len(str(n)) == 3:
        if int(str(n)[0]) + int(str(n)[1]) * 10 + int(str(n)[2]) * 100 == n:
            print("yes")
        else:
            print("no")
    elif len(str(n)) == 4:
        if int(str(n)[0]) + int(str(n)[1]) * 10 + int(str(n)[2]) * 100 + int(str(n)[3]) * 1000 == n:
            print("yes")
        else:
            print("no")
    else:
        if int(str(n)[0]) + int(str(n)[1]) * 10 + int(str(n)[2]) * 100 + int(str(n)[3]) * 1000 + int(str(n)[4]) * 10000 == n:
            print("yes")
        else:
            print("no")