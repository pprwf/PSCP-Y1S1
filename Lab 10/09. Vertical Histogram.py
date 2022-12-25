'''vert'''

def vertical(txt, alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    '''vert'''
    result = {}
    for i in alphabets:
        result[i] = 0
        for j in txt:
            if j == i:
                result[i] += 1
    highest = result[max(result, key=result.get)]
    for i in range(highest, 0, -1):
        print("%03d" %i, end='')
        for j in alphabets:
            if result[j] >= i and result[j] != 0:
                print(" *", end='')
            elif result[j] == 0:
                continue
            else:
                print("  ", end='')
        print()
    print(" " * 3, end='')
    for i in alphabets:
        if result[i] != 0:
            print(" %s" %i, end='')
vertical(input())
