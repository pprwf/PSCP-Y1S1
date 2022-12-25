'''rmtag'''

def remove_tag(tag):
    '''remove tag'''
    lis = []
    want = []
    for i in tag:
        if "@" not in i:
            lis.append(i)
    lis = " ".join(lis).split(" ")
    for i in lis:
        if i != "":
            want.append(i)
    print(want)
remove_tag(input().replace("<", "?@").replace(">", "@?").split("?"))
