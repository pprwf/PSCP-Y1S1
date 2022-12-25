'''diamond'''

def diamond(deep, width):
    '''diamond'''
    value = []
    cost = []
    for _ in range(deep):
        digging = input().split()
        value.append(digging)
    for i in range(width):
        num = 0
        for j in value:
            num += int(j[i])
        cost.append(num)
    print(max(cost))
diamond(int(input()), int(input()))
