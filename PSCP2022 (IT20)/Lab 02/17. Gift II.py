'''gift'''

def gift(wwa, wwb, wwc, wwd):
    '''gift'''
    if wwa % 2 == 0:
        print(wwa)
    elif wwb % 2 == 0:
        print(wwb)
    elif wwc % 2 == 0:
        print(wwc)
    elif wwd % 2 == 0:
        print(wwd)
    gift2(int(input()), int(input()), int(input()), int(input()))

def gift2(wwe, wwf, wwg, wwh):
    '''second gift'''
    if wwe % 2 == 0:
        print(wwe)
    elif wwf % 2 == 0:
        print(wwf)
    elif wwg % 2 == 0:
        print(wwg)
    elif wwh % 2 == 0:
        print(wwh)
gift(int(input()), int(input()), int(input()), int(input()))
