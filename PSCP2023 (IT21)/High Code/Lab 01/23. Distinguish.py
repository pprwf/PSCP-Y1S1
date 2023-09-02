'''Distinguish'''

def distinguish(height):
    '''function'''
    print("You're hit the door edge." if height > 180 else "Nothing happens.")
distinguish(int(input()))
