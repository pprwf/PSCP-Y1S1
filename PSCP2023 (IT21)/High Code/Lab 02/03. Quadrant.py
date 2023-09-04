'''Quadrant'''

def quad(x_point, y_point):
    '''Quadrant'''
    print("O" if x_point == y_point == 0 else "Y" if x_point == 0 else "X" if y_point == 0 else \
    "Q1" if x_point > 0 and y_point > 0 else "Q2" if x_point < 0 and y_point > 0 else "Q3" if \
    x_point < 0 and y_point < 0 else "Q4")
quad(int(input()), int(input()))
