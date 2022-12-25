'''Kayak'''

def boat():
    '''kayak'''
    int(input())
    total = 0
    weight = input().split(" ")
    for i in range(len(weight)):
        weight[i] = int(weight[i])
    weight = sorted(weight)
    weight.remove(max(weight))
    weight.remove(max(weight))
    for i in range(1, len(weight), 2):
        total += (weight[i] - weight[i - 1])
    print(total)
boat()
