'''quad'''

def quad(xline, yline):
    '''quad'''
    if xline == 0 and yline == 0:
        print("O")
    if xline == 0 and yline != 0:
        print("Y")
    if xline != 0 and yline == 0:
        print("X")
    if xline > 0 and yline > 0:
        print("Q1")
    if xline > 0 and yline < 0:
        print("Q4")
    if xline < 0 and yline < 0:
        print("Q3")
    if xline < 0 and yline > 0:
        print("Q2")
quad(int(input()), int(input()))
