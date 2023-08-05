'''virus'''

def virus(txt):
    '''virus'''
    size = 0
    for i in txt:
        if "o" == i:
            size += 1
    print(size)
virus(input())
