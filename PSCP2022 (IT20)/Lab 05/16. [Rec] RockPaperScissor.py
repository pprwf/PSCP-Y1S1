'''game'''

def rps(option, aaa=0, bbb=0):
    '''battle'''
    for i in range(0, len(option), 2):
        if option[i] == "r" and option[i + 1] == "s":
            aaa += 1
        elif option[i] == "r" and option[i + 1] == "p":
            bbb += 1
        if option[i] == "p" and option[i + 1] == "r":
            aaa += 1
        elif option[i] == "p" and option[i + 1] == "s":
            bbb += 1
        if option[i] == "s" and option[i + 1] == "p":
            aaa += 1
        elif option[i] == "s" and option[i + 1] == "r":
            bbb += 1
    if aaa > bbb:
        print("A win %d-%d" %(aaa, bbb))
    elif aaa < bbb:
        print("B win %d-%d" %(bbb, aaa))
    else:
        print("DRAW %d" %aaa)
rps(input().lower())
