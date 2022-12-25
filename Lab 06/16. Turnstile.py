'''Turnstile'''

def turn(action, status="locked", count=0):
    '''Turnstile'''
    while action != "END":
        if status == "locked":
            if action == "C":
                status = "unlocked"
        if status == "unlocked":
            if action == "P":
                status = "locked"
                count += 1
        action = input()
    print(count)
turn(input().upper())
