'''BMIAgain'''

def body_mass():
    '''BMIAgain'''
    weight = int(input())
    height = int(input())
    bmi = weight / (height * 0.01) ** 2
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")
body_mass()
