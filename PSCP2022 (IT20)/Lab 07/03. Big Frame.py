'''big frame'''

def frame(frame1, frame2, frame3, frame4, frame5):
    '''frame'''
    highest = max(len(frame1), len(frame2), len(frame3), len(frame4), len(frame5))
    print("*" * (highest + 4))
    print("* " + frame1 + " " * (highest - len(frame1)) + " *")
    print("* " + frame2 + " " * (highest - len(frame2)) + " *")
    print("* " + frame3 + " " * (highest - len(frame3)) + " *")
    print("* " + frame4 + " " * (highest - len(frame4)) + " *")
    print("* " + frame5 + " " * (highest - len(frame5)) + " *")
    print("*" * (highest + 4))
frame(input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip())
