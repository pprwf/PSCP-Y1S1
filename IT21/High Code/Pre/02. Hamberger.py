'''[Pre] Hamberger'''

def hamberger(left, right):
    '''0 star'''
    print("|" * left + "*" * ((left + right)* 2) + "|" * right)
hamberger(int(input()), int(input()))
