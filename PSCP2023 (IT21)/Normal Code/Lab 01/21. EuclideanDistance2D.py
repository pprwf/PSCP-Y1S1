'''Euclid'''

def euclid():
    '''euclid distance 2d'''
    numq1 = float(input())
    numq2 = float(input())
    nump1 = float(input())
    nump2 = float(input())
    print(((numq1 - nump1) ** 2 + (numq2 - nump2) ** 2) ** 0.5)
euclid()
