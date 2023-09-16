'''Brick Bridge'''

def brick():
    '''Brick Bridge'''
    small = int(input())
    big = int(input())
    goal = int(input())
    buse = goal // 5
    use = 0
    if buse >= big:
        goal %= 5
        print("Buse =", buse)
        print("Goal =", goal)
    if small < goal:
        use = -1
    else:
        use = small
    print(use)
brick()
