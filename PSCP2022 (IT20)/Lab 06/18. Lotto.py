'''lottory'''

def lotto(first, right2, left3_1, left3_2):
    '''gambling'''
    right3_1, right3_2, buy, prize = int(input()), int(input()), input(), 0
    if int(buy) == first:
        prize += 6000000
    if int(buy[-2:]) == right2:
        prize += 2000
    if int(buy[:3]) == left3_1 or int(buy[:3]) == left3_2 or\
        int(buy[-3:]) == right3_1 or int(buy[-3:]) == right3_2:
        prize += 4000
    if (first == 0 and (int(buy) == 1 or int(buy) == 999999)) or\
        (first == 999999 and (int(buy) == 0 or int(buy == 999998))):
        prize += 100000
    elif int(buy) + 1 == int(first) or int(buy) - 1 == int(first):
        prize += 100000
    print(prize)
lotto(int(input()), int(input()), int(input()), int(input()))
