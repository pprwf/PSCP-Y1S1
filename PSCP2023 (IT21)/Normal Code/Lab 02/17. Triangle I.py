'''Triangle I'''

def triangle():
    '''Triangle I'''
    one = float(input())
    two = float(input())
    three = float(input())
    if one > two:
        one, two = two, one
    if two > three:
        two, three = three, two
    if one > two:
        one, two = two, one
    if three - 0.01 <= (one ** 2 + two ** 2) ** 0.5 <= three + 0.01:
        print("Yes")
    else:
        print("No")
triangle()
