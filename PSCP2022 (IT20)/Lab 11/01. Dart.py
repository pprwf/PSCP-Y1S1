'''dart'''

def dart(times, score=0):
    '''dart'''
    for _ in range(times):
        pos = input().split(" ")
        ranges = (int(pos[0]) ** 2 + (int(pos[1])) ** 2) ** 0.5
        if ranges <= 2:
            score += 5
        elif ranges <= 4:
            score += 4
        elif ranges <= 6:
            score += 3
        elif ranges <= 8:
            score += 2
        elif ranges <= 10:
            score += 1
    print(score)
dart(int(input()))
