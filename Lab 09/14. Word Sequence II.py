'''wsii'''

def word():
    """wsii"""
    txt1 = input()
    txt2 = input()
    for i in range(0, max(len(txt1), len(txt2)) + 1):
        print(txt2[:i] + txt1[i:])
word()
