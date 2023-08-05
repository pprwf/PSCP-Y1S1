'''saitama'''

def saitama(push, sit, stand, run):
    '''exercise'''
    least1 = push / int(input())
    least2 = sit / int(input())
    least4 = run / int(input())
    least3 = stand / int(input())

    for _ in range(4):
        if least1 <= least2:
            least1, least2 = least2, least1
        if least2 <= least3:
            least2, least3 = least3, least2
        if least3 <= least4:
            least3, least4 = least4, least3
    print(int(least1 + 0.999999999))
saitama(int(input()), int(input()), int(input()), int(input()))
