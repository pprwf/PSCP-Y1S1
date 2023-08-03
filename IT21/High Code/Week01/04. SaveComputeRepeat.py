'''SaveComputeRepeat'''

def time(mill=492137954293754252786):
    '''SaveComputeRepeat'''
    sec, mill = mill // 1000, mill % 1000
    minute, sec = sec // 60, sec % 60
    hours, minute = minute // 60, minute % 60
    days, hours = hours // 24, hours % 24
    print(days, hours, minute, sec, mill)
time()
