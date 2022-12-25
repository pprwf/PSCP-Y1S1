"""Composite Fuction"""
 
def func():
    '''main function'''
    valx = int(input())
    print("%.2f" %(ffunc(gfunc(valx))))
    print("%.2f" %(gfunc(ffunc(valx))))
 
def ffunc(valx):
    '''f(x)'''
    return 2 * valx
 
def gfunc(valx):
    '''g(x)'''
    return valx / 2 + 1
func()
