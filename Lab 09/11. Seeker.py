'''seeker'''

def seek():
    """seeker"""
    txt = input()
    checking = ""
    val = 0
    for i in txt:
        if i.isdigit() == True:
            checking += i
        else:
            if checking == "":
                val += 0
            else:
                val += int(checking)
                checking = ""
    if checking.isdigit() == True:
        print(val + int(checking))
    else:
        print(val)
seek()
