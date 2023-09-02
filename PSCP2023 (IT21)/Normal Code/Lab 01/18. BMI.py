'''BMI'''

def bmi():
    '''BMI'''
    name = input()
    body = float(input()) / (float(input()) * 0.01) ** 2
    return name + "'s  BMI = %.2f" %body

def analyze():
    ''''output'''
    fst = bmi()
    snd = bmi()
    trd = bmi()
    fth = bmi()
    fif = bmi()
    print(fst)
    print(snd)
    print(trd)
    print(fth)
    print(fif)
analyze()
