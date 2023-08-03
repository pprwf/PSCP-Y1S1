'''[Pre] Left Arrow'''

def left_arrow():
    '''1 star'''
    width = int(input())
    height = int(input())
    for i in range(height):
        print(" " * abs(height // 2 - i) + "*" * width)
left_arrow()
