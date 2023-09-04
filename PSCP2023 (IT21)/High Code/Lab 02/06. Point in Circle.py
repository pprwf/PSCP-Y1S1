'''Point in Circle'''

def circle(center_x, center_y, radius, x_point, y_point):
    '''Point in Circle'''
    print(True if (x_point - center_x) ** 2 + (y_point - center_y) ** 2 <= radius ** 2 else False)
circle(float(input()), float(input()), float(input()), float(input()), float(input()))
