# 1018_체스판 다시 칠하기.py

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
min_count = None
for a in range(n-7):
    for b in range(m-7):
        count_b = 0
        count_w = 0
        for i in range(8):
            for j in range(0, 8, 2):
                if i % 2 == 0:
                    if board[i+a][j+b] != 'W':
                        count_w += 1
                else:
                    if board[i+a][j+b] != 'B':
                        count_w += 1
            for j in range(1, 8, 2):
                if i % 2 == 0:
                    if board[i+a][j+b] != 'B':
                        count_w += 1
                else:
                    if board[i+a][j+b] != 'W':
                        count_w += 1
        for i in range(8):
            for j in range(0, 8, 2):
                if i % 2 == 0:
                    if board[i+a][j+b] != 'B':
                        count_b += 1
                else:
                    if board[i+a][j+b] != 'W':
                        count_b += 1
            for j in range(1, 8, 2):
                if i % 2 == 0:
                    if board[i+a][j+b] != 'W':
                        count_b += 1
                else:
                    if board[i+a][j+b] != 'B':
                        count_b += 1
        if count_b < count_w:
            count = count_b
        else:
            count = count_w
            
        if min_count is None:
            min_count = count
        else:
            min_count = min(min_count, count)

print(min_count)