'''[Pre] Left Arrow'''

def left_arrow(width, height):
    '''1 star'''
    print(*[" " * abs(height // 2 - i) + "*" * width for i in range(height)], sep="\n")
left_arrow(int(input()), int(input()))
