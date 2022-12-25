'''clock'''

def clock(hour, sec):
    '''clock'''
    hour *= 5
    hour += sec / 12
    hour %= 60
    print(sec <= hour < sec + 1)
clock(int(input()), int(input()))
