'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''

def new_plan(string, num, num2, num3):
    '''sort the number'''
    num, num2 = (num2, num) if num > num2 else (num, num2)
    num2, num3 = (num3, num2) if num2 > num3 else (num2, num3)
    num, num2 = (num2, num) if num > num2 else (num, num2)
    num, num2, num3 = (num3, num2, num) if string == "Descend" else (num, num2, num3)
    print("%.2f, %.2f, %.2f" %(num, num2, num3))
new_plan(input(), float(input()), float(input()), float(input()))
