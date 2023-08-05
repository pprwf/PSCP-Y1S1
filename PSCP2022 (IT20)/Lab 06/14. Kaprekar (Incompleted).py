'''wtf'''

def kapre(kaprekar, num=1):
    '''idk'''
    most, two, three, least = int(kaprekar[0]), int(kaprekar[0]), int(kaprekar[0]), int(kaprekar[0])
    while kaprekar != "6174":
        if len(kaprekar) < 4:
            kaprekar += "0"
        for i in kaprekar:
            if int(i) > least:
                least = int(i)
                continue
            if int(i) >= least:
                three = int(i)
                continue
            if int(i) >= three:
                two = int(i)
                continue
            if int(i) > most:
                most = int(i)
                continue
        print(most, two, three, least)
        return
    
kapre(input())
