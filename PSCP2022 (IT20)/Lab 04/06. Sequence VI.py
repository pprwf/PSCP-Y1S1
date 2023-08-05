'''seq'''

def seq6(num):
    '''seq 6'''
    val = 1
    for _ in range(num):
        for i in range(1, val + 1):
            print(i, end=" ")
        print()
        val += 1
seq6(int(input()))
