'''parity'''

def parity(base2, oddeven, value=0):
    '''parity'''
    for i in base2:
        if i == "1":
            value += 1
    if value % 2 == 0:
        if oddeven == "Even":
            print(base2 + "0")
        elif oddeven == "Odd":
            print(base2 + "1")
    else:
        if oddeven == "Even":
            print(base2 + "1")
        elif oddeven == "Odd":
            print(base2 + "0")
parity(input(), input().capitalize())
