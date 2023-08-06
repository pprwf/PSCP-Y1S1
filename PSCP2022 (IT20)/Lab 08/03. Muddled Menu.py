'''mud'''

def mud():
    '''muddled'''
    menu = []
    while True:
        meal = input()
        if meal == "DONE":
            break
        elif meal == "SOMETHING'S WRONG":
            menu.clear()
        elif "Can't do: " in meal:
            menu.remove(meal[10:])
        elif meal == "CLOSED":
            return print("Full Course: [] Reversed: []")
        else:
            splitter = meal.split(" #")
            if splitter[1].isnumeric():
                menu.insert(int(splitter[1]) - 1, splitter[0])
            else:
                menu.append(splitter[0])
    print("Full Course:", menu, end="")
    menu.reverse()
    print(" Reversed:", menu)
mud()
