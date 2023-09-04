'''Point in Circle'''

def circle():
    '''Point in Circle'''
    center_x = float(input())
    center_y = float(input())
    circle_radius = float(input())
    x_point = float(input())
    y_point = float(input())
    if (x_point - center_x) ** 2 + (y_point - center_y) ** 2 <= circle_radius ** 2:
        print(True)
    else:
        print(False)
circle()
