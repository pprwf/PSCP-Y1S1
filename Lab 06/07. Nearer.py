'''itim'''

def icecream(alice, bob, ice):
    '''bob & alice'''
    alice_dis = abs(ice - alice)
    bob_dis = abs(ice - bob)
    if alice_dis > bob_dis:
        print("Bob %d" %bob_dis)
    elif bob_dis > alice_dis:
        print("Alice %d" %alice_dis)
    elif alice_dis == bob_dis:
        print("Sundaes %d" %bob_dis)
icecream(int(input()), int(input()), int(input()))
