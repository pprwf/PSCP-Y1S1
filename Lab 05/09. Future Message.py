'''future'''

def future():
    '''message'''
    txt = input()
    if txt.isnumeric():
        print("Number")
    elif txt.islower():
        print("Lowercase")
    elif txt.isupper():
        print("Uppercase")
    elif txt.istitle():
        print("Title")
    elif txt.isspace():
        print("Space")
    else:
        print("Other")
future()
