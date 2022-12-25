'''blackjack'''

def gambling(score=0, ace=0):
    '''gambling'''
    for _ in range(int(input())):
        card = input()
        if card.isnumeric():
            score += int(card)
        if card == "J" or card == "Q" or card == "K":
            score += 10
        if card == "A":
            score += 11
            ace += 1
    while ace != 0 and score > 21:
        score -= 10
        ace -= 1
    print(score)
gambling()
