'''Euclid'''

def euclid(numq1, numq2, nump1, nump2):
    '''euclid distance 2d'''
    print(((numq1 - nump1) ** 2 + (numq2 - nump2) ** 2) ** 0.5)
euclid(float(input()), float(input()), float(input()), float(input()))
