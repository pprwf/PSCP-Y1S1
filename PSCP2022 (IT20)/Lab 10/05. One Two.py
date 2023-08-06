'''onetwo'''

def onetwo(num, min2="1", min1="2", txt=""):
    '''onetwo'''
    if num == 1:
        return print(1)
    elif num == 2:
        return print(2)
    for _ in range(3, num + 1):
        txt = min1 + min2
        min2, min1 = min1, txt
    print(txt)
onetwo(int(input()))
