'''def'''

def pick(txt):
    '''pick them'''
    lis = []
    for i in txt.split(", "):
        if int(i) % 2 == 0:
            lis.append(i)
    if lis == []:
        print("Nope")
    else:
        for i in lis:
            print(i)
pick(input()[1:-1])
