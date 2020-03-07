t = int(input())
result = []
score = 0
score_count = 1

for i in range(t):
    ox = input()
    ox_len = len(ox)
    
    for j in range(ox_len):
        if ox[j] == 'O':
            score += score_count
            score_count += 1
        else:
            score_count = 1
        
    result.append(score)
    score = 0
    score_count = 1

for i in range(t):
    print(result[i])