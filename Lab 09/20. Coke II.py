'''coke'''

def coke(cost, lid, special, amount):
    """coke"""
    if lid == 0:
        print(cost*amount)
        quit()
    if amount == 0:
        print(0)
        quit()
    value = (amount - 1)
    loop = value // lid
    left = value % lid
    price = (cost*(lid-1)) + special
    total = cost + (loop * price) + (left * cost)
    print(total)
coke(int(input()), int(input()), int(input()), int(input()))
