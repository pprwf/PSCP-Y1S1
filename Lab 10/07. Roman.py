'''roman'''

def main(txt, trans=0):
    '''roman'''
    dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    for i, j in enumerate(txt):
        if (i + 1) == len(txt) or dic[j] >= dic[txt[i+1]]:
            trans += dic[j]
        else:
            trans -= dic[j]
    print(trans)
main(input())
