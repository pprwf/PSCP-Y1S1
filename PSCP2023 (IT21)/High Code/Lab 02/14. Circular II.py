'''Circular II'''

def two_circle(my_x, my_y, rad, your_x, your_y):
    '''Circular II'''
    print("No" if ((your_x - my_x) ** 2 + (your_y - my_y) ** 2) ** 0.5 >= rad + float(input()) \
        else "Yes")
two_circle(float(input()), float(input()), float(input()), float(input()), float(input()))
