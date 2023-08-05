'''inflation'''

def inflat(money, year):
    '''money'''
    money = int(money * 100)
    for _ in range(year):
        money += (money * 381 // 10000)
    print("%d.%02d" %(money // 100, money % 100))
inflat(float(input()), int(input()))
