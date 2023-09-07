'''WeightStation'''

def station(avg, tire, tire2, tire3):
    '''WeightStation'''
    high, low, miss = round(avg + avg / 2), round(avg - avg / 2) + 1, avg * 4 - tire - tire2 - tire3
    print("Overweight" if avg * 4 > 15000 else "Unbalance"\
    if tire not in range(low, high) or tire2 not in range(low, high) or \
    tire3 not in range(low, high) or miss not in range(low, high) else "Pass %.2f" %miss)
station(float(input()), float(input()), float(input()), float(input()))
