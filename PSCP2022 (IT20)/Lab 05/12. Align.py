'''align'''
 
def zombie(size, posit, txt):
    '''zombie'''
    if posit == "left":
        print(txt + " " * (size - len(txt)))
    if posit == "center":
        left, right = (size - len(txt)) // 2, (size - len(txt)) // 2
        if (size - len(txt)) % 2 != 0:
            left += 1
        print(" " * left + txt + " " * right)
    if posit == "right":
        print(" " * (size - len(txt)) + txt)
zombie(int(input()), input().lower(), input())
