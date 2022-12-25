'''grade'''

def convert(score, val=0):
    '''convert'''
    if 60 > score >= 0:
        val = 0
    if 65 > score >= 60:
        val = 0.5
    if 70 > score >= 65:
        val = 1
    if 75 > score >= 70:
        val = 1.5
    if 80 > score >= 75:
        val = 2
    if 85 > score >= 80:
        val = 2.5
    if 90 > score >= 85:
        val = 3
    if 95 > score >= 90:
        val = 3.5
    if 95 <= score <= 100:
        val = 4
    return val

def grade(num, avg=0):
    '''grade'''
    for _ in range(num):
        avg += convert(float(input()))
    print("%.2f" % (int((avg / num) * 100) / 100))
grade(int(input()))
