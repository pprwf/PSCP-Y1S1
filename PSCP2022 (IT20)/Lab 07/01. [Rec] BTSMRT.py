'''train'''
 
def train(day, age, height):
    '''train'''
    if age < 14 and height <= 140 and day == "Children Day" or age < 14 and\
height < 90 or age >= 60 and day == "Senior Day":
        print("FREE")
    else:
        print("PAY")
train(input(), float(input()), float(input()))
