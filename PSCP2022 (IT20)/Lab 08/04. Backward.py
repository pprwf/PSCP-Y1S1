'''backward'''

def back():
    '''back'''
    lis = []
    while True:
        lis.append(input())
        if lis[-1] == "NULL":
            lis.pop()
            break
    lis.reverse()
    for i in lis:
        print(i)
back()
