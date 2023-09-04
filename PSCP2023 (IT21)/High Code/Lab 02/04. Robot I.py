'''Robot I'''

def robot(name, age):
    '''Robot I'''
    print("%s, you" %name, "can pass." if age < 18 else "shall not pass.")
robot(input(), float(input()))
