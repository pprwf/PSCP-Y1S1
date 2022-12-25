'''robot'''

def machine(name, age):
    '''robot'''
    if age < 18:
        print("%s, you can pass." %name)
    else:
        print("%s, you shall not pass." %name)
machine(input(), float(input()))
