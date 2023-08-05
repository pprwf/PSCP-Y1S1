'''point'''

def circle(xxx, xyy, xrr, xxn, xyn):
    '''circle'''
    if ((xxn - xxx) ** 2 + (xyy - xyn) ** 2) ** 0.5 <= xrr:
        print("True")
    else:
        print("False")
circle(float(input()), float(input()), float(input()), float(input()), float(input()))
