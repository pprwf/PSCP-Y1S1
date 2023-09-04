'''Quadrant'''

def quad():
    '''Quadrant'''
    x_point = int(input())
    y_point = int(input())
    if x_point == y_point == 0:
        print("O")
    elif x_point == 0:
        print("Y")
    elif y_point == 0:
        print("X")
    elif x_point > 0 and y_point > 0:
        print("Q1")
    elif x_point < 0 and y_point > 0:
        print("Q2")
    elif x_point < 0 and y_point < 0:
        print("Q3")
    else:
        print("Q4")
quad()
