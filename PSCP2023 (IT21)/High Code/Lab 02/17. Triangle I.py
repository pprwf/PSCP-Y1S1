'''Triangle I'''

def triangle(one, two, three):
    '''Triangle I'''
    if one > two:
        one, two = two, one
    if two > three:
        two, three = three, two
    if one > two:
        one, two = two, one
    print("Yes" if three - 0.01 <= (one ** 2 + two ** 2) ** 0.5 <= three + 0.01 else "No")
triangle(float(input()), float(input()), float(input()))
