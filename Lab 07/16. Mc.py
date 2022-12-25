'''mac'''

def mac(code, valid=None):
    '''mac'''
    for i, j in enumerate(code.replace("-", "").replace(":", "").replace(".", "")):
        if i == 11 and valid is not False:
            valid = True
        if j not in "ABCDEF0123456789":
            valid = False
    if valid:
        if len(code) == 17 and (code[2::3]) == "-----":
            print("VALID 1")
        elif len(code) == 17 and (code[2::3]) == ":::::":
            print("VALID 2")
        elif len(code) == 14 and (code[4::5]) == "..":
            print("VALID 3")
        else:
            print("ERROR")
    else:
        print('ERROR')
mac(input().upper())
