'''Boomerang'''

def boom(num_x, num_y, num_z):
    '''Boomerang'''
    print(num_x + 1)
    print(7 * num_y ** 3 + 2 * num_y ** 2 - 31 * num_y + 1)
    print(- num_z)
    print((num_x + num_y) * (num_x - num_y))
    print((num_y - (num_y ** 2 - 4 * num_x * num_z) ** 0.5) / (2 * num_x))
boom(int(input()), int(input()), int(input()))
