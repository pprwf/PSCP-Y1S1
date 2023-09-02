'''BMI'''

def bmi():
    '''BMI'''
    return input() + "'s  BMI = %.2f" %(float(input()) / (float(input()) * 0.01) ** 2)

def analyze():
    ''''output'''
    print(bmi(), bmi(), bmi(), bmi(), bmi(), sep="\n")
analyze()
