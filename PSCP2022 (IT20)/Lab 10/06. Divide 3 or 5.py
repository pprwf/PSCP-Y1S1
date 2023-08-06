'''def'''

def divide(num, total=0):
    '''divide'''
    for i in range(1, int(num) + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)
divide(float(input()))
