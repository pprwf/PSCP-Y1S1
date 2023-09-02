'''TheFunctionWithin'''

def ffunc(num):
    '''f'''
    return 2 * num

def gfunc(num):
    '''g'''
    return 3 * num ** 4 - num ** 3 + 2 * num ** 2 + 10

def hfunc(x_num, y_num, z_num):
    '''h'''
    return (z_num + x_num) ** 2 - x_num * y_num + y_num ** 2

def ifunc(a_num, b_num, c_num, d_num):
    '''i'''
    return (a_num ** 2 + b_num ** 2 - c_num ** 2) / (d_num ** 2 - 2 * a_num * d_num + 2 * a_num)

def comp():
    '''composite'''
    a_num = float(input())
    b_num = float(input())
    c_num = float(input())
    d_num = float(input())
    print(ffunc(ffunc(a_num)))
    print(gfunc(ffunc(a_num - b_num)))
    print(hfunc(ffunc(a_num + b_num), ffunc(a_num + c_num), gfunc(ffunc(d_num ** 2))))
    print(ifunc(hfunc(ffunc(a_num + b_num), ffunc(a_num - c_num), gfunc(ffunc(d_num ** 2))),
                gfunc(ffunc(a_num - b_num)), ffunc(ffunc(ffunc(ffunc(ffunc(c_num))))), d_num ** 8))
comp()
