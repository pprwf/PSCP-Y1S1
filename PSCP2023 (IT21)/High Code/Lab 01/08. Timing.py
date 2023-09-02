'''Timing'''

def second(sec):
    '''Timing'''
    print(sec // 86400, sec // 3600 % 24, sec // 60 % 60, sec % 60)
second(int(input()))
