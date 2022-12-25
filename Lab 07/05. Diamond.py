'''diamond'''

def diamond(size, special=1):
    '''diamond'''
    length, space = size // 2, size // 2
    for i in range(length):
        if i == 0:
            print(" " * space + "*", end="")
        else:
            print(" " * space + "*" + " " * special + "*", end="")
            if special >= 1:
                force_sp = special
            special += 2
        space -= 1
        print()
    print("*" * size)
    space += 1
    for i in range(length):
        if i == 0 and special > 1:
            special = force_sp
        if i == length - 1:
            print(" " * space + "*", end="")
        else:
            print(" " * space + "*" + " " * special + "*", end="")
            special -= 2
        space += 1
        print()
diamond(int(input()))
