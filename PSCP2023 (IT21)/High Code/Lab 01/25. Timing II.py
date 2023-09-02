'''Timing II'''

def timing(time):
    '''Timing II'''
    day, hour, minute = time // 86400, time // 3600 % 24, time // 60 % 60
    print("ERR_:__:__:__" if day > 9999 else "%04d:%02d:%02d:%02d" %(day, hour, minute, time % 60))
timing(int(input()))
