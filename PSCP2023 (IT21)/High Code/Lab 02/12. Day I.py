'''Day I'''

def day(year):
    '''Day I'''
    print("Yes" if (not year % 4 and year % 100) or not year % 400 else "No")
day(int(input()))
