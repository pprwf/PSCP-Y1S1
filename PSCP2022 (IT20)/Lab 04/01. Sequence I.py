'''seq'''

def seq1(num):
    '''seq 1'''
    for _ in range(num):
        for i in range(1, num + 1):
            print(i, end=" ")
        print()
seq1(int(input()))
