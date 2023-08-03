'''[Pre] Hamberger'''

def hamberger():
    '''0 star'''
    left = int(input())
    right = int(input())
    meat = (left + right) * 2
    print("|" * left, end="")
    print("*" * meat, end="")
    print("|" * right)
hamberger()
