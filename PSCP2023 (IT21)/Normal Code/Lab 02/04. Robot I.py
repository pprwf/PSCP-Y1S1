'''Robot I'''

def robot():
    '''Robot I'''
    name = input()
    age = float(input())
    if age < 18:
        print("%s, you can pass." %name)
    else:
        print("%s, you shall not pass." %name)
robot()
