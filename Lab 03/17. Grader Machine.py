'''even'''

def machine(start, stop, txt="pass : ", result=0):
    '''machine'''
    if start < stop:
        for i in range(start, stop + 1):
            if not i % 2:
                txt += str(i) + " "
                result += i
    else:
        for i in range(start, stop - 1, -1):
            if not i % 2:
                txt += str(i) + " "
                result += i
    print(txt)
    print("Sum : %d" %result)
machine(int(input()), int(input()))
