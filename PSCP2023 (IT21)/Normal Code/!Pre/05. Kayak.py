'''[Pre] Kayak'''

def kayak():
    '''3 star'''
    num = int(input())
    weight = input().split(" ")
    total = 0
    for i in range(len(weight)):
        weight[i] = int(weight[i])
    weight.sort()
    for _ in range(num - 1):
        diff = []
        for i in range(1, len(weight)):
            diff.append(weight[i] - weight[i - 1])
        total += min(diff)
        del_value = diff.index(min(diff))
        del weight[del_value:del_value + 2]
    print(total)
kayak()
