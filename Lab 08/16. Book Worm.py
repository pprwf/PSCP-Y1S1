'''book worm'''

def book(value):
    '''book'''
    for _ in range(value):
        time = float(input())
        amount = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(amount)):
            if sum(amount[:i+1]) > time:
                break
            i += 1
        print(i)
book(int(input()))
