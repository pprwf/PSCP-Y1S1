'''weight'''

def station(avg, ww1, ww2, ww3):
    '''station'''
    weight = avg * 4
    ww4 = weight - ww1 - ww2 - ww3
    con1 = weight > 15000
    con2 = avg - avg / 2 > ww1 or ww1 > avg + avg / 2
    con3 = avg - avg / 2 > ww2 or ww2 > avg + avg / 2
    con4 = avg - avg / 2 > ww3 or ww3 > avg + avg / 2
    con5 = avg - avg / 2 > ww4 or ww4 > avg + avg / 2
    if con1 or con1 and (con2 or con3 or con4 or con5):
        print("Overweight")
    elif con2 or con3 or con4 or con5:
        print("Unbalance")
    else:
        print("Pass %.2f" %ww4)
station(float(input()), float(input()), float(input()), float(input()))
