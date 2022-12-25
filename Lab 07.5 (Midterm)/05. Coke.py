'''coke'''

def coke(cost, lid, new, want, money=0):
    '''coke'''
    cap, price = 0, cost
    while want > 0:
        cap += 1
        money += price
        price = cost
        if lid == 0:
            money = cost * want
            break
        if cap == lid:
            price = new
            cap = 0
        want -= 1
    print(money)
coke(int(input()), int(input()), int(input()), int(input()))
