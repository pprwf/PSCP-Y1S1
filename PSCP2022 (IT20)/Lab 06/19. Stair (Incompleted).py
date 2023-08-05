'''stair'''

def stair(can, smt, step=0):
    '''stair'''
    height = int(input())
    for _ in range(smt - 1):
        total = int(input())
        if height > can or total > can:
            print("NO")
            return
        if height + total > can:
            height = total
            step += 1
        elif height + total == can:
            step += 1
            height = 0
        else:
            height += total
    print(step)
stair(int(input()), int(input()))
