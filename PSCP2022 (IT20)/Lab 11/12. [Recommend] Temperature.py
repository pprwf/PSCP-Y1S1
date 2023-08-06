'''temperature'''

def convert(temp, unit):
    '''convert'''
    if unit == "r":
        temp = (temp - 491.67) * (5 / 9)
    elif unit == "f":
        temp = (temp - 32) * (5 / 9)
    elif unit == "k":
        temp -= 273.15
    return temp

def temperature(temp, have, need):
    '''rec'''
    if have != "c":
        temp = convert(temp, have)
    if need == "c":
        print("%.2f" %temp)
    elif need == "f":
        print("%.2f" %((temp * 1.8) + 32))
    elif need == "k":
        print("%.2f" %(temp + 273.15))
    elif need == "r":
        print("%.2f" %((temp + 273.15) * (9 / 5)))
temperature(float(input()), input().lower(), input().lower())
