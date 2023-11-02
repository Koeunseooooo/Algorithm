# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
n = int(input())
card = list(map(int, input().split()))
card_len = len(card)
card.sort()
m = int(input())
card2 = list(map(int, input().split()))

for choiced_card in card2:
    left = 0
    right = len(card)
    if 
