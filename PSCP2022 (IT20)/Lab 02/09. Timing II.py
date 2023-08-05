'''Timing'''

def time(sec):
    '''timing'''
    if sec // 86400 > 9999:
        print("ERR_:__:__:__")
        return
    print("%04d:%02d:%02d:%02d" %(sec // 86400, sec % 86400 // 3600,
                                  sec % 86400 % 3600 // 60, sec % 60))
time(int(input()))
