'''christ'''

def tree(leaf, log, asterisk=1):
    '''tree'''
    baseleaf = leaf - 1
    for _ in range(leaf):
        print(" " * baseleaf, end="")
        print("*" * asterisk)
        asterisk += 2
        baseleaf -= 1
    for _ in range(log):
        print(" " * (leaf - 2), end="")
        print("---")
tree(int(input()), int(input()))
