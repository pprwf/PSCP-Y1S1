'''donut'''

def donut(price, amount, bonus, least):
    '''donut'''
    value = amount + bonus
    cost = price * amount
    num = least // value
    remain = least - (num * value)
    if remain >= amount:
        num += 1
        remain = 0
    print("%d %d" %(num * cost + remain * price, num * value + remain))
donut(int(input()), int(input()), int(input()), int(input()))
