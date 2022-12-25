'''def'''

def pick(txt):
    '''pick them'''
    lis = []
    for i in txt.split(" "):
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            lis.append(i)
    if lis == []:
        print("Nope")
    else:
        lis.reverse()
        for i in lis:
            print(i)
pick(input())
