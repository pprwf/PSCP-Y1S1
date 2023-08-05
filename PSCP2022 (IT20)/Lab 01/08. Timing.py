'''timing'''

def time(sec):
    '''time'''
    day, hrs, minute = int(sec / 60 / 60 // 24), int(sec / 60 / 60 % 24), \
((sec % 86400) % 3600) // 60
    print(day, hrs, minute, sec % 60)
time(int(input()))
