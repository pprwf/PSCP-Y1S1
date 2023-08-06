'''area'''

def area(count=0):
    '''AREA'''
    for _ in range(int(input())):
        for i in input():
            if i != " ":
                count += 1
    print(count)
area()
