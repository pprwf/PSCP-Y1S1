'''letter'''

import string

def letter():
    """letter"""
    text = input().lower().replace(" ", "")
    value = list(filter(lambda a: a in string.ascii_letters, text))
    value = max(set(text), key=text.count)
    print(value)
letter()
