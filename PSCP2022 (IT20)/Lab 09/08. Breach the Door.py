'''door'''

def door():
    """breach the door"""
    print(*filter(lambda a: len(a) > 6, (["".join(j for j in i if \
    j.isalpha()) for i in input().split(" ")])))
door()
