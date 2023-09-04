'''Seven'''

def seven():
    '''seven ** expo'''
    exponential = int(input())
    mod = exponential % 4
    if mod == 1:
        print(7)
    elif mod == 2:
        print(9)
    elif mod == 3:
        print(3)
    else:
        print(1)
seven()
