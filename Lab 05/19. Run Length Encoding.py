'''encode'''

def encode(txt, code="", num=0, txt2=""):
    '''encode'''
    for i in range(len(txt) - 1):
        if txt[i] != txt[i + 1]:
            txt2 += txt[i]
    for i in txt2:
        for j in range(len(txt)):
            if txt[j] == i:
                num += 1
            else:
                code += str(num) + i
                txt = txt[j:]
                num = 0
                break
    print(code)
encode(input() + "1")
