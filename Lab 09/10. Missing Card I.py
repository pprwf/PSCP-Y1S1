'''missing card'''

def missing():
    """card"""
    lis = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card = []
    for i in lis:
        card_s = i + "S"
        card_h = i + "H"
        card_d = i + "D"
        card_c = i + "C"
        card.append(card_s)
        card.append(card_h)
        card.append(card_d)
        card.append(card_c)
    for _ in range(51):
        miss = str(input())
        if miss in card:
            card.remove(miss)
    print(card[0])
missing()
