'''four'''

def second_lines(txt):
    '''nd'''
    for i in txt:
        if i == "U":
            print(" ***  ", end="")
        if i == "D":
            print("  *   ", end="")
        if i == "L":
            print(" *    ", end="")
        if i == "R":
            print("   *  ", end="")
    print()

def third_lines(txt):
    '''rd'''
    for i in txt:
        if i == "U" or i == "D":
            print("* * * ", end="")
        if i == "L" or i == "R":
            print("***** ", end="")
    print()

def fourth_lines(txt):
    '''th'''
    for i in txt:
        if i == "U":
            print("  *   ", end="")
        if i == "D":
            print(" ***  ", end="")
        if i == "L":
            print(" *    ", end="")
        if i == "R":
            print("   *  ", end="")
    print()

def direction(txt):
    '''direction'''
    print("  *   " * len(txt))
    second_lines(txt)
    third_lines(txt)
    fourth_lines(txt)
    print("  *   " * len(txt))
direction(input().upper())
