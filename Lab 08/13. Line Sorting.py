'''line sorting'''

def liso(line):
    '''nert'''
    lis = []
    for _ in range(line):
        lis.append(input())
    lis.sort(key=len)
    for i in lis:
        print(i)
liso(int(input()))
