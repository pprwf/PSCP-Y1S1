'''seq 5'''

def seq5(num):
    '''seq 5'''
    for _ in range(num):
        if num == 0:
            break
        for _ in range(7):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
seq5(int(input()))
