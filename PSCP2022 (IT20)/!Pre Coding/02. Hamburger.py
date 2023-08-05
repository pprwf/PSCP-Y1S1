'''ham'''

def burger(left, right):
    '''burger'''
    print("|" * left + "**" * (left + right) + "|" * right)
burger(int(input()), int(input()))
