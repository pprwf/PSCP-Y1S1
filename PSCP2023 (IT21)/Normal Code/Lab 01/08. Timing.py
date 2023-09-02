'''Timing'''

def second():
    '''Timing'''
    sec = int(input())
    day = sec // 60 // 60 // 24
    hour = sec // 60 // 60 % 24
    minute = sec // 60 % 60
    sec %= 60
    print(day, hour, minute, sec)
second()
