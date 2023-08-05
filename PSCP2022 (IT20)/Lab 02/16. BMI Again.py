'''again?'''

def bmi(weight, height):
    '''bmi'''
    if weight / (height / 100) ** 2 < 18.5:
        print("Underweight")
    elif 18.5 <= weight / (height / 100) ** 2 < 25:
        print("Normal")
    elif 25 <= weight / (height / 100) ** 2 < 30:
        print("Overweight")
    elif weight / (height / 100) ** 2 >= 30:
        print("Obese")
bmi(int(input()), int(input()))
