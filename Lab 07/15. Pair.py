'''pair'''

def pair(dancing, val="", alone="", counting=0):
    '''pair'''
    for i in dancing:
        if val.count(i) <= 0:
            val += i
    for i in val:
        if (int(dancing.count(i)) % 2) == 1:
            counting += 1
            alone += i
    print('fully paired' if counting == 0 else alone)
pair(input().lower())
