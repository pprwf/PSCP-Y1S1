'''MyMath'''
from math import sin, cos, log2, log10
from math import radians as rad
from math import factorial as fac
from math import log as lg

def mymath():
    '''MyMath'''
    print((sin(rad(90)) + sin(rad(60)) ** 2) / (cos(rad(245 ** 2)) + cos(rad(45 + 135))))
    print(fac(16) * fac(4) / fac(8))
    print((15 + 25) / ((25 - 12) ** 2 + (12 - 15) ** 2) ** 0.5)
    print(log10(1234 ** 4))
    print((lg(4234, 5) + log2(8191) + 71 * log10(156154)) / (lg(777, 7) - lg(888, 8) - lg(999, 9)))
mymath()
