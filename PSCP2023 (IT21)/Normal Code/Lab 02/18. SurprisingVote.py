'''SurprisingVote Not Complete'''

def vote():
    '''SurprisingVote'''
    total = float(input())
    high = float(input())
    least = (total - high) / 2
    if high * 2 < total:
        least = total - high * 2
    if high - least > 2:
        print("Surprising")
    else:
        print("Not surprising")
vote()
