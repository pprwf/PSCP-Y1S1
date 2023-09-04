'''Gift II'''

def gift(box, count, even):
    '''Gift II'''
    even = box if not box % 2 else even
    count += (count < 8)
    return gift(int(input()), count, even) if count != 8 else even
print(gift(int(input()), 0, 0))
