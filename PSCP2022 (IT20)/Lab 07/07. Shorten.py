'''shorten'''

def short(num1=0, num2=1, txt=""):
    '''short'''
    true_then_false = True
    while True:
        num = int(input())
        if num == -1:
            if true_then_false:
                print()
            else:
                txt += str(num1 + num2 - 1)
            break
        if true_then_false:
            true_then_false = False
            num1 = num
        else:
            if num1 + num2 == num:
                if num2 == 1:
                    txt += str(num1) + '-'
                num2 += 1
            else:
                txt += str(num1 + num2 - 1) + ', '
                num1 = num
                num2 = 1
    print(txt)
short()
