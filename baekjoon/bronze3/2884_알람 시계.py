import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if h == 0 and m == 45 :
    ans_a = 0
    ans_b = 0
elif h == 0 and m < 45 :
    ans_a = 23
    ans_b = 60-(45-m)
elif m < 45 :
    ans_a = h-1
    ans_b = 60-(45-m)
else:
    ans_a = h
    ans_b = m-45

print(ans_a, ans_b)

