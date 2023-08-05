'''Parallelogram'''

def parallel(txt, space=" "):
    '''no'''
    num = len(txt) - 1
    for i in range(len(txt) - 1):
        print(space * num + txt[:i + 1])
        num -= 1
    print(txt)
    for i in range(- len(txt), -1):
        print(txt[i + 1:])
parallel(input())
