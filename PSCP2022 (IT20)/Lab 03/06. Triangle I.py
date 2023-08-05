'''trian'''

def three(l01, l02, l03):
    '''three side'''
    if l01 > l02:
        l01, l02 = l02, l01
    if l03 < l02:
        l03, l02 = l02, l03
    if l02 < l01:
        l01, l02 = l02, l01
    if l03 <= (l01 ** 2 + l02 ** 2) ** 0.5 <= l03 + 0.01:
        print("Yes")
    else:
        print("No")
three(float(input()), float(input()), float(input()))
