'''Largest Number'''

def largest():
    '''Largest Number'''
    one = input()
    two = input()
    three = input()
    big = int(one + two + three)
    if big < int(one + three + two):
        big = int(one + three + two)
    if big < int(two + one + three):
        big = int(two + one + three)
    if big < int(two + three + one):
        big = int(two + three + one)
    if big < int(three + one + two):
        big = int(three + one + two)
    if big < int(three + two + one):
        big = int(three + two + one)
    print(big)
largest()
