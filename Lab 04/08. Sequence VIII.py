'''seq 8'''

def seq8(num):
    '''seq 8'''
    space = num - 1
    txt = 1
    for _ in range(num):
        for _ in range(space):
            print("  ", end=" ")
        for i in range(txt):
            print("%02d" %(i + 1), end=" ")
        print()
        space -= 1
        txt += 1
seq8(int(input()))
