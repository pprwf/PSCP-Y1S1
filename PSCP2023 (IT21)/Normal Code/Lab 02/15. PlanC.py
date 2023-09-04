'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''

def new_plan():
    '''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
    string = input()
    number1 = float(input())
    number2 = float(input())
    number3 = float(input())
    if number1 > number2:
        number1, number2 = number2, number1
    if number2 > number3:
        number2, number3 = number3, number2
    if number1 > number2:
        number1, number2 = number2, number1
    if string == "Ascend":
        print("%.2f, %.2f, %.2f" %(number1, number2, number3))
    else:
        print("%.2f, %.2f, %.2f" %(number3, number2, number1))
new_plan()
