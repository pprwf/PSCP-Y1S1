'''day 1 - honne'''

def day(year):
    '''she so cute'''
    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        print("Yes")
    else:
        print("No")
day(int(input()))
