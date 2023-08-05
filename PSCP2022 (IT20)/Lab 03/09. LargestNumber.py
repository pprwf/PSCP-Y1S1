'''largenum'''

def compare_number(val1, val2):
    """comp"""
    if val1 > val2:
        return val1
    return val2

def num(num1, num2, num3):
    '''largenum'''
    biggestt = num1 + num2 + num3
    biggestt = compare_number((num1 + num3 + num2), biggestt)
    biggestt = compare_number((num2 + num1 + num3), biggestt)
    biggestt = compare_number((num2 + num3 + num1), biggestt)
    biggestt = compare_number((num3 + num2 + num1), biggestt)
    biggestt = compare_number((num3 + num1 + num2), biggestt)
    print(int(biggestt))
num(input(), input(), input())
