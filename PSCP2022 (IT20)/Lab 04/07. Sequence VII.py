'''seq 7'''

def seq7(num):
    '''seq'''
    val = 2
    for _ in range(num):
        for i in range(1, val):
            print(i, end=" ")
        print()
        val += 1
    for _ in range(num - 1):
        for i in range(1, val - 2):
            print(i, end=" ")
        print()
        val -= 1
seq7(int(input()))
