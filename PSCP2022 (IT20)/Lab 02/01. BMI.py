'''BMI Calculate'''
 
def inp(name, weight, height):
    '''input'''
    return "%s's  BMI = %.2f" %(name, weight / ((height / 100) ** 2))
 
def main():
    '''Main'''
    print(inp(input(), float(input()), float(input())))
    print(inp(input(), float(input()), float(input())))
    print(inp(input(), float(input()), float(input())))
    print(inp(input(), float(input()), float(input())))
    print(inp(input(), float(input()), float(input())))
main()
