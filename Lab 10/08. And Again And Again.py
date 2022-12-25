'''again'''

def again(vowel="aeiou"):
    '''again'''
    lis = []
    for i in input().split(" "):
        val = 0
        if "." in i:
            i = i.split(".")[0]
        for j in i:
            if j in vowel:
                val += 1
            if val >= 2:
                lis.append(i)
                break
    if lis == []:
        return print("Nope")
    for i in sorted(lis):
        print(i)
again()
