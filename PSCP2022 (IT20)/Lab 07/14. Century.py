'''century'''

from math import ceil

def cen():
    '''century'''
    for _ in range(int(input())):
        year = input()
        num = ""
        if "B.E." in year:
            for i in year:
                if i.isnumeric():
                    num += i
            num = int(num) - 543
        elif "A.D." in year:
            for i in year:
                if i.isnumeric():
                    num += i
            num = int(num)
        if num < 1:
            print("ERROR")
            continue
        elif num > 0 and num <= 100:
            print(1)
        else:
            print(ceil(num / 100))
cen()
