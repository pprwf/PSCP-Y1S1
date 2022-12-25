'''missing'''

def miss(val):
    '''missing number'''
    num = []
    for i in range(1, val):
        num.append(i)
    while True:
        given = int(input())
        if given == 0:
            break
        num.remove(given)
    for i in num:
        print(i)
miss(int(input()) + 1)
