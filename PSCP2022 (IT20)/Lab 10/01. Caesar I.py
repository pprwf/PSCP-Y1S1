'''caesar'''
import string as s

def caesar(num, txt, translate=""):
    '''caesar'''
    for i in txt:
        if i in s.ascii_letters:
            if i.isupper():
                translate += chr((ord(i) - ord("A") + num) % 26 + ord("A"))
            else:
                if i != " ":
                    translate += chr((ord(i) - ord("a") + num) % 26 + ord("a"))
                else:
                    translate += i
        else:
            translate += i
    print(translate)
caesar(int(input()), input())
