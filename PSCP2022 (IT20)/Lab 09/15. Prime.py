'''small'''

def smol(num):
    '''small'''
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0 and num != 2:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
smol(int(input()))
