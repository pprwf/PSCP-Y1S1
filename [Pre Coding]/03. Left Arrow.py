'''left arrow'''

def main(width, height):
    '''arrow'''
    for i in range(height // 2):
        print(" " * int(height // 2 - i) + "*" * width)
    print("*" * (width))
    for i in range(1, height // 2 + 1):
        print(" " * i + "*" * width)
main(int(input()), int(input()))
