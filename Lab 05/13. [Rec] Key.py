'''key'''

def key(card_id, total=0):
    '''key'''
    for i in card_id:
        total += int(i)
    total += int(card_id[10:]) * 10
    if total > 9999:
        print(str(total)[-4:])
    elif total < 1000:
        print(total + 1000)
    else:
        print(total)
key(input())
