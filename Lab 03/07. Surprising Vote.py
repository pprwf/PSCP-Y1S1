'''surprise'''

def vote(total, high):
    '''def'''
    another = (total - high) / 2
    if high * 2 < total:
        another = total - high * 2
    if high - another > 2:
        print("Surprising")
    else:
        print("Not surprising")
vote(float(input()), float(input()))
