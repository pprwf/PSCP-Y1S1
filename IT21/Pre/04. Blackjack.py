'''[Pre] Blackjack'''

def twenty_one():
    '''2 star'''
    card = int(input())
    score = 0
    ace = 0
    for _ in range(card):
        num = input()
        if num in ["J", "Q", "K"]:
            score += 10
        elif num == "A":
            score += 11
            ace += 1
        else:
            score += int(num)
    while ace != 0 and score > 21:
        score -= 10
        ace -= 1
    print(score)
twenty_one()
