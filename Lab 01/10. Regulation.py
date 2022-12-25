'''regu'''

def reg(inp1, inp2, inp3):
    '''reg'''
    print(" " * (30 - len(str(inp1))) + str(inp1))
    print(str(inp1).zfill(30))
    print("%.2f" %inp2)
    print("%.12f" %inp2)
    print(" " * (40 - len(inp3)) + inp3)
reg(int(input()), float(input()), input())
