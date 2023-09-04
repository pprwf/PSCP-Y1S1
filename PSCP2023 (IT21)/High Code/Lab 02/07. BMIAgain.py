'''BMIAgain'''

def body_mass(bmi):
    '''BMIAgain'''
    print("Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else\
        "Obese")
body_mass(int(input()) / (int(input()) / 100) ** 2)
