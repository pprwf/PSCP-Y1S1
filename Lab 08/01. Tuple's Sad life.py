'''tuple'''

def tup(txt, txt2):
    '''tuple'''
    for _ in range(txt.count(txt2)):
        for _ in range(txt.count(txt2)):
            print(txt.index(txt2), end=" ")
        print()
tup(tuple(input().split()), input())
