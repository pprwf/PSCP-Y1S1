'''FoodGrade I'''

def check(weight, count, mix):
    '''check weight'''
    mix += 1 if 50 <= weight <= 70 else 0
    count += (count < 24)
    return check(int(input()), count, mix) if count != 24 else mix
print(check(int(input()), 0, 0))
