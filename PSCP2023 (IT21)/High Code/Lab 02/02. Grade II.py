'''Grade II'''

def grading(score):
    '''grading ii'''
    print("ERR" if score > 100 or score < 0 else "A" if 95 <= score <= 100 else "B+" \
        if 90 <= score else "B" if 85 <= score else "C+" if 80 <= score else "C" if 75 <= score \
        else "D+" if 70 <= score else "D" if 65 <= score else "F+" if 60 <= score else "F")
grading(float(input()))
