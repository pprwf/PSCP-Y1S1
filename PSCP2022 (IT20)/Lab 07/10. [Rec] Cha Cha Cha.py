'''hometown'''

def cha(day, won=0):
    '''cha cha cha'''
    for _ in range(day):
        hour = float(input())
        if hour % 1 != 0:
            hour = hour // 1 + 1
        won += 8720 * hour
    print(int(won))
cha(int(input()))
