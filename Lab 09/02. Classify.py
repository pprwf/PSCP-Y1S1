'''class'''

def classify():
    '''class'''
    stu_id = []
    while True:
        val = input()
        if val == "END":
            break
        stu_id.append(val[:4])
    year = 0
    for i in sorted(set(stu_id)):
        newyear = i[:2]
        print(newyear if newyear != year else "--", int(i[2:4]), stu_id.count(i))
        year = newyear
classify()
