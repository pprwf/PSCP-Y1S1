'''parade'''

def cat():
    '''cat parade'''
    parade = []
    while True:
        inp = input()
        if inp == "END":
            break
        if inp == "IT'S A DOG":
            parade.pop()
            continue
        if ", " in inp:
            for i in range(len(inp.split(", "))):
                parade.append(inp.split(", ")[i])
        else:
            parade.append(inp)
    sort_list = []
    for i in sorted(parade):
        if i not in sort_list:
            sort_list.append(i)
    for i in sort_list:
        print(i, parade.index(i) + 1, parade.count(i))
cat()
