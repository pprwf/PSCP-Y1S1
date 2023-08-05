'''milk'''

def milk(cost, pro, trade, money):
    '''milk'''
    value = money // cost
    val = value
    if pro != 0:
        while True:
            val += trade * (value // pro)
            value = value % pro + trade * (value // pro)
            if value < pro:
                break
    print(val)
milk(int(input()), int(input()), int(input()), int(input()))
