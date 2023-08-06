'''kabata'''

def kabata(val):
    '''kabata'''
    for _ in range(val):
        txt = input().replace('baka', '-').replace("bakka", "").replace("ta", "")\
.replace("ba", "").replace("ka", "")
        if txt == "":
            print("yes")
        else:
            print("no")
kabata(int(input()))
