'''seq 9'''

def seq9(num):
    '''seq'''
    space = num - 1
    txt = 2
    for _ in range(num):
        for _ in range(space):
            print("  ", end=" ")
        for i in range(1, txt):
            print("%02d" %i, end=" ")
        for i in range(txt - 2, 0, -1):
            print("%02d" %i, end=" ")
        space -= 1
        txt += 1
        print()
seq9(int(input()))
