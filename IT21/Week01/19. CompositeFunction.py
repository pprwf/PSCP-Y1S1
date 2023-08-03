'''CompositeFunction'''

def ffunc(num):
    '''f'''
    return 2 * num

def gfunc(num):
    '''g'''
    return num / 2 + 1

def comp():
    '''main func'''
    num = int(input())
    print("%.2f" %ffunc(gfunc(num)))
    print("%.2f" %gfunc(ffunc(num)))
comp()
