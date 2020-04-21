# 2822_점수 계산.py
# 구현

import sys
input = sys.stdin.readline

score = []
for i in range(8):
    score.append((int(input()), i+1))
score.sort(reverse=True)

result = []
total = 0
for i in range(5):
    result.append(score[i])
    total += score[i][0]
result.sort(key=lambda x: int(x[1]))

print(total)
for i in range(5):
    print(result[i][1], end=' ')