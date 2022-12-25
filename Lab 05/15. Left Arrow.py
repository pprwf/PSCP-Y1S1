'''left arrow'''

def left(width, height):
    '''arrow'''
    top_space = height // 2
    bottom_space = 0 - top_space
    for _ in range(height):
        if top_space > 0:
            print(" " * top_space + "*" * width)
        if top_space == 0:
            print("*" * width)
        if bottom_space > 0:
            print(" " * bottom_space + "*" * width)
        top_space -= 1
        bottom_space += 1
left(int(input()), int(input()))
