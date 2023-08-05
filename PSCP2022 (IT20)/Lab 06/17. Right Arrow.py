'''right arrow'''

def arrow(width, height, space=0):
    '''right'''
    for _ in range(height // 2):
        print(" " * space + "*" * width)
        space += 1
    print(" " * space + "*" * width)
    for _ in range(height // 2):
        space -= 1
        print(" " * space + "*" * width)
arrow(int(input()), int(input()))
