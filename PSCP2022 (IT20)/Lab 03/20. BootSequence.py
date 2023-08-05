'''boot'''

def boot(num):
    '''sequence'''
    for ixn in range(1, num + 1):
        if ixn == num:
            print(ixn)
            break
        print(ixn, end="_")
boot(int(input()))
