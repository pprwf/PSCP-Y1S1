'''second grade'''

def grade(score):
    '''grade'''
    if score < 0 or score > 100:
        print("ERR")
    elif 0 >= score or score < 60:
        print("F")
    elif 60 >= score or score < 65:
        print("F+")
    elif 65 >= score or score < 70:
        print("D")
    elif 70 >= score or score < 75:
        print("D+")
    elif 75 >= score or score < 80:
        print("C")
    elif 80 >= score or score < 85:
        print("C+")
    elif 85 >= score or score < 90:
        print("B")
    elif 90 >= score or score < 95:
        print("B+")
    elif 95 >= score or score < 100:
        print("A")
grade(float(input()))
