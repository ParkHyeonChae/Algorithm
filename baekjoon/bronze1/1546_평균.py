n = int(input())
score = list(map(int, input().split()))
new_score = []
score_sum = 0

m = max(score)

for i in range(n):
    new = score[i]/m*100
    new_score.append(new)

for i in range(n):
    score_sum += new_score[i]

print(score_sum/n)