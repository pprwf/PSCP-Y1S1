'''meteor'''

def meteorite(weight, split, notdanger, missile=0):
    '''meteorite'''
    new_split = split
    if weight >= notdanger:
        missile = 1
    while weight >= notdanger:
        weight /= split
        if weight >= notdanger:
            for _ in range(new_split):
                missile += 1
        new_split *= split
    print(missile)
meteorite(float(input()), int(input()), float(input()))
