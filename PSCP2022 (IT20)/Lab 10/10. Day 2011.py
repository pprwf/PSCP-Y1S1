'''dnm'''

def daynmonth(date, month):
    '''daynmonth'''
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month - 1):
        date += months[i]
    if date % 7 == 0:
        print("Friday")
    elif date % 7 == 1:
        print("Saturday")
    elif date % 7 == 2:
        print("Sunday")
    elif date % 7 == 3:
        print("Monday")
    elif date % 7 == 4:
        print("Tuesday")
    elif date % 7 == 5:
        print("Wednesday")
    elif date % 7 == 6:
        print("Thursday")
daynmonth(int(input()), int(input()))
