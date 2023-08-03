'''[Pre] Kayak'''

def kayak(num, weight, total=0):
    '''3 star'''
    for _ in range(num - 1):
        diff = [weight[i] - weight[i - 1] for i in range(1, len(weight))]
        total += min(diff)
        del weight[diff.index(min(diff)):diff.index(min(diff)) + 2]
    print(total)
kayak(int(input()), sorted([int(i) for i in input().split(" ")]))
