'''invert'''

def invert(txt, new=""):
    '''inverter'''
    for i in txt:
        if i == "0":
            new += "1"
        elif i == "1":
            new += "0"
    if not "1" in new:
        return None
    print(new[new.find("1"):])
invert(input())
