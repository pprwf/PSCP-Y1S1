'''calc'''

def calc(val):
    """calc"""
    count = len(str(val))
    count_1 = 1
    count_9 = 9
    tap_num = 0
    if val == 1:
        print(1)
        quit()
    for i in range(1, count):
        howmany = (count_9 - count_1)+1
        tap_num += howmany * i
        count_1 = int(str(count_1) + "0")
        count_9 = int(str(count_9) + "9")
    last_count = ((val - count_1) + 1) * count
    total = (tap_num + last_count) + val
    print(total)
calc(int(input()))
