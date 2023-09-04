'''DataSpike'''

def spike(data, count, highest):
    '''Data Spiky'''
    highest = data if highest < data else highest
    count += (count < 8)
    return spike(int(input()), count, highest) if count != 8 else highest
print(spike(int(input()), 0, 0))
