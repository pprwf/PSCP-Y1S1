'''FOR!F-Ball'''

def swap(posit, ball=1):
    '''rec'''
    for i in posit:
        if i == "a":
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif i == "b":
            if ball == 3:
                ball = 2
            elif ball == 2:
                ball = 3
        elif i == "c":
            if ball == 1:
                ball = 3
            elif ball == 3:
                ball = 1
    print(ball)
swap(input().lower())
