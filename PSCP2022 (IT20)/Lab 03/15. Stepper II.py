'''stepper 2'''

def stepper(start, stop):
    '''stepper 2'''
    if start < stop:
        for i in range(start, stop + 1):
            print(i)
    else:
        for i in range(start, stop - 1, -1):
            print(i)
stepper(int(input()), int(input()))
