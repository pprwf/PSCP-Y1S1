'''dup'''

def dupli(mnum, nnum):
    '''dup'''
    seta, same = set(), []
    for _ in range(mnum):
        seta.add(int(input()))
    for _ in range(nnum):
        stu = int(input())
        if stu in seta:
            same.append(stu)
    if len(same) == 0:
        print("Nope")
    else:
        same.sort()
        same.reverse()
        for i in same:
            print(i)
dupli(int(input()), int(input()))
