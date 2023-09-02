'''Rectangle'''

def area(height, width):
    '''area of rectangle'''
    print(height * width)

def peri(height, width):
    '''perimeter of rectangle'''
    print(2 * height + 2 * width)

def rect():
    '''Rectangle'''
    height = int(input())
    width = int(input())
    area(height, width)
    peri(height, width)
rect()
