'''[Pre] Blackjack'''

def twenty_one(score=0, ace=0):
    '''2 star'''
    for _ in range(int(input())):
        num = input()
        score += 10 if num in ["J", "Q", "K"] else 11 if num == "A" else int(num)
        ace += 1 and num == "A"
    while ace != 0 and score > 21:
        score -= 10
        ace -= 1
    print(score)
twenty_one()
