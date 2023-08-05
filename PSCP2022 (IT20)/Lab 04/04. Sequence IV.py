'''seq 4'''

def seq4(num):
    '''seq'''
    valx = 1
    for _ in range(1, num ** 2 + 1, num): 
        for _ in range(1, num + 1):
            print(valx, end=" ")
            valx += 1
        print()
seq4(int(input()))
