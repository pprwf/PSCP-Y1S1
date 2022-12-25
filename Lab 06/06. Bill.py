'''Bill'''

def bill(total):
    '''bill'''
    services = total * 10 / 100
    if services < 50:
        total += 50
    elif services <= 1000:
        total += services
    elif services > 1000:
        total += 1000
    total *= 1.07
    print('%.2f'%total)
bill(int(input()))
