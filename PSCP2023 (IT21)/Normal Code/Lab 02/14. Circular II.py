'''Circular II'''

def two_circle():
    '''Circular II'''
    my_x = float(input())
    my_y = float(input())
    my_radius = float(input())
    your_x = float(input())
    your_y = float(input())
    your_radius = float(input())
    if ((your_x - my_x) ** 2 + (your_y - my_y) ** 2) ** 0.5 >= my_radius + your_radius:
        print("No")
    else:
        print("Yes")
two_circle()
