'''harshad'''
 
def harshad(total=0):
    '''num'''
    for _ in range(10):
        num = int(input())
        if num > 0:
            for i in range(len(str(num))):
                total += int(str(num)[i])
            if num % total == 0:
                print("Yes")
                total = 0
            else:
                print("No")
                total = 0
        elif num < 0:
            for i in range(1, len(str(num))):
                total += int(str(num)[i])
            if num % total == 0:
                print("Yes")
                total = 0
            else:
                print("No")
                total = 0
        else:
            print("No")
harshad()
