'''หรม'''

def horrormor(first, second):
    '''หรม'''
    for i in range(100000, 0, -1):
        if first % i == 0 and second % i == 0:
            print(i)
            break
horrormor(int(input()), int(input()))
