'''rule of three'''

def rule(amount=0, worthyprice=0, worthysize=0):
    '''rule'''
    for _ in range(int(input())):
        price = float(input())
        weight = float(input())
        if weight / price > amount:
            amount = weight / price
            worthyprice = price
            worthysize = weight
        if weight / price == amount:
            if worthyprice > price:
                worthyprice = price
                worthysize = weight
    print("%.2f %.2f" %(worthyprice, worthysize))
rule()
