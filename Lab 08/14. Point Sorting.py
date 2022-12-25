'''def'''

def point(num):
    '''point sorting'''
    for _ in range(num):
        val = int(input())
        lis = []
        for _ in range(val):
            txt = input().split()
            new_list = []
            new_list.append(int(txt[0]))
            new_list.append(int(txt[1]))
            lis.append(new_list)
        lis.sort(reverse=True, key=lambda lis: lis[1])
        lis.sort(key=lambda lis: lis[0]+lis[1])
        for i in lis:
            for j in i:
                print(j, end=" ")
            print()
point(int(input()))
