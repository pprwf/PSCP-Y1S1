'''binary'''

def bnary(num):
    '''binary'''
    lis = []
    if num == 0:
        return print(0)
    while num > 0:
        lis.append(str(num % 2))
        num //= 2
    lis.reverse()
    print("".join(lis))
bnary(int(input()))
