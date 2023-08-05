'''netflix'''

def package(premium, standard, basic, mobile, total):
    '''package'''
    if premium > 0:
        print("Premium x %d" %premium)
    if standard > 0:
        print("Standard x %d" %standard * (standard > 0))
    if basic > 0:
        print("Basic x %d" %basic * (basic > 0))
    if mobile > 0:
        print("Mobile x %d" %mobile * (mobile > 0))
    print("Total = %d THB" %total)

def netflix(screen, phone):
    '''netflix'''
    input()
    input()
    television = input().lower()
    hd_screen = input().lower()
    ultra = input().lower()
    count_premium = 0
    count_standard = 0
    count_basic = 0
    count_mobile = 0
    total = 0
    while screen > 0 or phone > 0:
        if (ultra == "yes" or hd_screen == "yes" or television == "yes") \
            and (screen >= 3 or phone >= 3):
            total += 419
            count_premium += 1
            screen -= 4
            phone -= 4
        elif (hd_screen == "yes" or television == "yes") \
            and (screen >= 2 or phone >= 2):
            total += 349
            count_standard += 1
            screen -= 2
            phone -= 2
        elif television == "yes" and ultra == "no" and hd_screen == "no":
            total += 279
            count_basic += 1
            screen -= 1
            phone -= 1
        else:
            if ultra == "yes":
                total += 419
                count_premium += 1
                screen -= 4
                phone -= 4
            elif hd_screen == "yes":
                total += 349
                count_standard += 1
                screen -= 2
                phone -= 2
            elif television == "yes":
                total += 279
                count_basic += 1
                screen -= 1
                phone -= 1
            else:
                total += 99
                count_mobile += 1
                screen -= 1
                phone -= 1
    package(count_premium, count_standard, count_basic, count_mobile, total)
netflix(int(input()), int(input()))
