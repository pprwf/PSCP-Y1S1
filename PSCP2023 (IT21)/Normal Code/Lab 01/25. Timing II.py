'''Timing II'''

def timing():
    '''Timing II'''
    time = int(input())
    day = time // 86400
    hour = time // 3600 % 24
    minute = time // 60 % 60
    second = time % 60
    if day <= 9999:
        print("%04d:%02d:%02d:%02d" %(day, hour, minute, second))
    else:
        print("ERR_:__:__:__")
timing()
