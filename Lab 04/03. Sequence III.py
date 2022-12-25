'''seq 3'''

def seq3(num):
    '''seq 1'''
    valx = 2
    for _ in range(num):
        for _ in range(num):
            print(valx, end=" ")
            valx += 1
        print()
        valx -= num - 1
seq3(int(input()))
