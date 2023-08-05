'''plan c'''
 
def plan(opt, num1, num2, num3):
    '''not plan a'''
    if num1 > num2:
        num1, num2 = num2, num1
    if num3 < num2:
        num3, num2 = num2, num3
    if num2 < num1:
        num1, num2 = num2, num1
    if opt == "Ascend":
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif opt == "Descend":
        print("%.2f, %.2f, %.2f" %(num3, num2, num1))
plan(input().title(), float(input()), float(input()), float(input()))
