'''elo'''

def elo(num1, num2, string):
    '''elo diff'''
    var_ea = 1 / (1 + 10 ** ((num2 - num1) / 400))
    var_eb = 1 / (1 + 10 ** ((num1 - num2) / 400))
    if string == "A":
        print("%.2f" %var_ea)
    else:
        print("%.2f" %var_eb)
elo(int(input()), int(input()), input().capitalize())
