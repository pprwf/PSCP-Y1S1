'''hamburger'''

def ham(left, right):
    '''ham'''
    print("|" * left + "*" * (left + right) * 2 + "|" * right)
ham(int(input()), int(input()))
