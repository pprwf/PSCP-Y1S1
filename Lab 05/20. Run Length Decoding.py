'''decode'''

def decode(txt, code=""):
    '''decode'''
    for i in txt:
        if i.isnumeric():
            code += i
        else:
            print(i * int(code), end="")
            code = ""
decode(input())
