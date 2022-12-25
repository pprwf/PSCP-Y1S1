'''almost'''

def almost(num):
    '''almost'''
    stuid = []
    score = []
    for _ in range(num):
        txt = input().split("\t")
        stuid.append(txt[0])
        score.append(float(txt[1]))
    mean = sum(score) / num
    score.append(mean)
    new_score = sorted(score)
    need = new_score[new_score.index(mean) - 1]
    print(stuid[score.index(need)] + "\t" + str(need))
almost(int(input()))
