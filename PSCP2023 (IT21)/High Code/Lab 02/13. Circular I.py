'''Circular I'''

def circle(my_x, my_y, rad, mos_x, mos_y):
    '''Circular I'''
    print("Yes" if ((mos_x - my_x) ** 2 + (mos_y - my_y) ** 2) ** 0.5 <= rad else "No")
circle(float(input()), float(input()), float(input()), float(input()), float(input()))
