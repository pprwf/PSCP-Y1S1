'''book'''

from math import ceil

def book(total, pages, num_x, num_y, day=0):
    '''book'''
    count, counter = 0, 0
    while True:
        val = ceil((num_x / num_y) * pages)
        if count == total:
            break
        if val >= pages:
            break
        counter += val
        if counter >= pages:
            counter = 0
            count += 1
        num_x += 1
        num_y += 1
        day += 1
    day += (total - count)
    print(day)
book(int(input()), int(input()), int(input()), int(input()))
