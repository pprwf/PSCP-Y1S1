'''rectangle'''
 
def length(width, height):
    '''length'''
    return width * 2 + height * 2
 
def area(width, height):
    '''area and length of rectangle'''
    if width > 0 < height:
        print(width * height)
        print(length(width, height))
area(int(input()), int(input()))
