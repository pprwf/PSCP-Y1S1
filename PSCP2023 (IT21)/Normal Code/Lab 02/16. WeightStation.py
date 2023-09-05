'''WeightStation'''

def station():
    '''WeightStation'''
    average = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    plus_average = round(average + average / 2)
    minus_average = round(average - average / 2)
    missing = average * 4 - weight1 - weight2 - weight3
    if average * 4 > 15000:
        print("Overweight")
    elif weight1 not in range(minus_average, plus_average + 1) or \
        weight2 not in range(minus_average, plus_average + 1) or \
        weight3 not in range(minus_average, plus_average + 1) or \
        missing not in range(minus_average, plus_average + 1):
        print("Unbalance")
    else:
        print("Pass %.2f" %missing)
station()
