'''food'''

def restaurant(price, pro, percent, add):
    '''food'''
    cost = price + add
    if cost >= pro:
        cost -= cost * (percent / 100)
    if cost == price or price == pro:
        print("Yes")
    elif cost > price:
        print("No %.3f" %(cost - price))
    else:
        print("Yes %.3f" %(price - cost))
restaurant(float(input()), float(input()), float(input()), float(input()))
