'''data spike'''

def dat(comp, num2, num3, num4):
    '''dat'''
    if comp < num2:
        comp = num2
    if comp < num3:
        comp = num3
    if comp < num4:
        comp = num4
    compare(int(input()), int(input()), int(input()), int(input()), comp)

def compare(num5, num6, num7, num8, comp):
    '''comparison'''
    if comp < num5:
        comp = num5
    if comp < num6:
        comp = num6
    if comp < num7:
        comp = num7
    if comp < num8:
        comp = num8
    print(comp)
dat(int(input()), int(input()), int(input()), int(input()))
