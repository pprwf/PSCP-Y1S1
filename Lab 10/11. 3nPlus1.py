'''3'''

def another(num):
    '''calc'''
    val = []
    while num != 1:
        val.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    val.append(1)
    return len(val)

def plus():
    '''plus'''
    lis = []
    while True:
        num = int(input())
        if num == 0:
            break
        lis.append(num)
    for i in lis:
        print(another(i))
plus()
