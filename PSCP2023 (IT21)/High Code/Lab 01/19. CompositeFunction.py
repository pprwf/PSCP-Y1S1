'''CompositeFunction'''

def ffunc(num):
    '''f'''
    return 2 * num

def gfunc(num):
    '''g'''
    return num / 2 + 1

def comp(num):
    '''main func'''
    print("%.2f\n%.2f" %(ffunc(gfunc(num)), gfunc(ffunc(num))))
comp(int(input()))
