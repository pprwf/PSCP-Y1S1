'''all prime'''

def prime(val=0):
    '''all'''
    for i in range(1, int(input()) + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                val += 1
    print(val)
prime()
