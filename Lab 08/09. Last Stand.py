'''last'''

def last(txt):
    '''last'''
    lis = []
    for i in txt.split(","):
        lis.append(i[-1])
    for i in lis:
        print(i)
last(input()[1:-1])
