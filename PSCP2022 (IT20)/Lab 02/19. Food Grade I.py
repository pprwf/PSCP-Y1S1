'''food'''

def food():
    '''grade'''
    good = 0
    good = nextfood(good)
    good = nextfood(good)
    good = nextfood(good)
    print(nextfood(good))

def nextfood(good):
    '''grade'''
    if 50 <= float(input()) <= 70:
        good += 1
    if 50 <= float(input()) <= 70:
        good += 1
    if 50 <= float(input()) <= 70:
        good += 1
    if 50 <= float(input()) <= 70:
        good += 1
    if 50 <= float(input()) <= 70:
        good += 1
    if 50 <= float(input()) <= 70:
        good += 1
    return good
food()
