'''circle'''
 
def circle(xx1, yy1, rad, xx2, yy2):
    '''circle'''
    if ((xx2 - xx1) ** 2 + (yy2 - yy1) ** 2) ** 0.5 >= rad + float(input()):
        print("No")
    else:
        print("Yes")
circle(float(input()), float(input()), float(input()), float(input()), float(input()))
