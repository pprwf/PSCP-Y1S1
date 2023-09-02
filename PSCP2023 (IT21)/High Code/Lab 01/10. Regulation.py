'''Regulation'''

def reg(int_a, float_b, str_c):
    '''Regulation'''
    print("%30d\n%030d\n%.2f\n%.12f\n%40s" %(int_a, int_a, float_b, float_b, str_c))
reg(int(input()), float(input()), input())
