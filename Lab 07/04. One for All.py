'''my hero'''

def hero(sequence, length=""):
    '''all might'''
    for i in range(1, sequence + 1):
        name = input()
        if i == sequence:
            length += name + "_" + str(i)
        elif i % 2:
            length += name + "*" * i
        else:
            length += name + "-" * i
    print(length)
hero(int(input()))
