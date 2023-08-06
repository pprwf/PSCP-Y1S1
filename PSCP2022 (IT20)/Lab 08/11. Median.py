'''median'''

def median(num):
    '''median'''
    number = []
    for _ in range(num):
        number.append(int(input()))
    number.sort()
    if num % 2 == 0:
        print("%.1f" %((number[(num // 2) - 1] + number[num // 2]) / 2))
    else:
        print("%.1f" %number[num // 2])
median(int(input()))
