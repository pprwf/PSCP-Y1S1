'''Donut'''

def donut():
    '''Donut'''
    price = int(input())
    promotion = int(input())
    free = int(input())
    least = int(input())
    amount = least // (promotion + free)
    
    cost = amount * price + least - (amount * (promotion + free))
    print("%d %d" %(cost))
donut()
