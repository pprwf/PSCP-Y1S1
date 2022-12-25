'''coprime'''

def prime():
    """cp"""
    val1 = int(input())
    val2 = int(input())
    check = 1
    for i in range(1, val1 + 1):
        if val1 % i == 0 and val2 % i == 0:
            check = i
    if check == 1:
        print("YES")
        print(check)
    else:
        print("NO")
        print(check)
prime()
