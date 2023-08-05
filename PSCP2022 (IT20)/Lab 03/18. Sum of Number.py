'''sum'''

def num(want, result=0):
    '''num'''
    inp = 0
    while inp != -1:
        result += inp
        if result == want:
            break
        inp = int(input())
    print(result)
num(int(input()))
