'''Heron of Alexandria'''

def heron(side_a, side_b, side_c):
    '''Alexandria'''
    var_s = (side_a + side_b + side_c) / 2
    print("%.3f" %((var_s * (var_s - side_a) * (var_s - side_b) * (var_s - side_c)) ** 0.5))
heron(float(input()), float(input()), float(input()))
