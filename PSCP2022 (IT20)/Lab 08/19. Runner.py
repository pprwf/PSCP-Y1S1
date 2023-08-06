'''runner'''

def run(distance, battle):
    '''runner'''
    lis = []
    runner = []
    for _ in range(battle):
        data = input().split(" ")
        lis.append(data)
    new_list = lis.copy()
    lis.sort(key=lambda i: float(i[0]), reverse=True)
    for i in lis:
        runner.append((distance-float(i[1]))/float(i[0]))
    print(new_list.index(lis[runner.index(min(runner))])+1)
run(float(input()), int(input()))
