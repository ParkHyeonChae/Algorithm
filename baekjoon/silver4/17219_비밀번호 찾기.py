# 17219_비밀번호 찾기.py

# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict(input().split() for _ in range(n))
print ("\n".join([dic[input()] for _ in range(m)]))