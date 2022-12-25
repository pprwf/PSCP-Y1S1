'''diginity'''

def digi(num, total=0):
    '''digit'''
    while num != "0":
        while len(num) != 1:
            for i in num:
                total += int(i)
            num = str(total)
            total = 0
        print(num)
        num = input()
digi(input())
