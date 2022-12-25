'''frame'''

def frame(txt):
    '''frame'''
    print("*" * (len(txt) + 2) + "\n*%s*\n" %txt + "*" * (len(txt) + 2))
frame(input())
