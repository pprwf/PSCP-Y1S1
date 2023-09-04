'''Circular I'''

def circle():
    '''Circular I'''
    my_x = float(input())
    my_y = float(input())
    radius = float(input())
    mosquito_x = float(input())
    mosquito_y = float(input())
    if ((mosquito_x - my_x) ** 2 + (mosquito_y - my_y) ** 2) ** 0.5 > radius:
        print("No")
    else:
        print("Yes")
circle()
