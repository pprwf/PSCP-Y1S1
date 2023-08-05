'''var'''

def valid(num):
    '''valid variable'''
    for _ in range(num):
        test = input()
        con1, con2, con3 = False, False, test[0].isnumeric()
        con4 = test == "if" or test == "else" or test == "elif" or test == "while" or test == "for"\
or test == "True" or test == "False" or test == "continue" or test == "break" or test == "return"\
or test == "is" or test == "in" or test == "and" or test == "or" or test == "from" or test == "as"\
or test == "pass" or test == "not" or test == "def" or test == "None"
        for i in test[1:-1]:
            if i == " ":
                con2 = True
        for i in "!()-[];:'\",<>./?\\@#$%^+=&*~":
            for j in test:
                if i == j:
                    con1 = True
                    break
        if con1 or con2 or con3 or con4:
            print("Invalid")
        else:
            print("Valid")
valid(int(input()))
