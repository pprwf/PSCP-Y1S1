'''math'''
 
from math import sin, cos, log, radians, factorial, sqrt
 
def math():
    '''math'''
    print((sin(radians(90)) + sin(radians(60)) ** 2) / (cos(radians(60025)) + cos(radians(180))))
    print(factorial(16) * factorial(4) / factorial(8))
    print((15 + 25) / sqrt((25 - 12) ** 2 + (12 - 15) ** 2))
    print(log(1234 ** 4, 10))
    print((log(4234, 5) + log(8191, 2) + 71 * log(156154, 10)) / (log(777, 7) - \
log(888, 8) - log(999, 9)))
math()
