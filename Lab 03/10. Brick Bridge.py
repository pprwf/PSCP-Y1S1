'''brick'''

def brick(small, big, goal):
    '''size'''
    goal //= 5
    if big >= goal:
        goal = goal-(goal*5)
    elif big < goal:
        goal = goal-(big*5)
    if small >= goal:
        print(goal)
    else:
        print(-1)
brick(int(input()), int(input()), int(input()))
