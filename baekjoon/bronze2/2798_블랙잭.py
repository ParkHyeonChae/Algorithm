from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
card_list = list(combinations(card, 3))
max_card = 0
card_sum = 0

for i in range(len(card_list)):
    card_sum = card_list[i][0] + card_list[i][1] + card_list[i][2]
    if m >= card_sum:
        max_card = max(max_card, card_sum)

print(max_card)