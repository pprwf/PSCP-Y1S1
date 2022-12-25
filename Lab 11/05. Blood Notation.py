'''blood'''

def blood(age, weight, past):
    '''blood'''
    if age == 17 or (age >= 60 and age <= 70):
        cert = input()
        if cert == "False":
            return print("No")
    if age >= 17 and age <= 70 and weight >= 45:
        if age > 55 and past == 0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
blood(int(input()), int(input()), int(input()))
