'''Blackjack'''

def dealer(hand, score=0, ace=0):
    '''gambling'''
    if 2 <= hand <= 3:
        for _ in range(hand):
            card = input()
            if card == "A":
                score += 11
                ace += 1
            elif card == "J" or card == "Q" or card == "K" or card == "10":
                score += 10
            elif card in "23456789":
                score += int(card)
    while ace != 0 and score > 21:
        score -= 10
        ace -= 1
    print(score)
dealer(int(input()))
