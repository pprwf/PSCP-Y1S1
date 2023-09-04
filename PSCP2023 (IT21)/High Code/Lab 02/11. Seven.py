'''Seven'''

def seven(expo):
    '''seven ** expo'''
    print(7 if expo == 1 else 9 if expo == 2 else 3 if expo == 3 else 1)
seven(int(input()) % 4)
