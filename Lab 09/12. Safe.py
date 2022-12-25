'''safe'''

def down(checkmark, locking, rotate_down=0):
    """Rotate down"""
    while locking != checkmark:
        if locking >= 25:
            locking = -1
        rotate_down += 1
        locking += 1
    return rotate_down
def upp(checkmark, locking):
    """Rotate up"""
    rotate_up = 0
    while locking != checkmark:
        if locking <= 0:
            locking = 26
        rotate_up += 1
        locking -= 1
    return rotate_up
def safe(correct, lock):
    """Safe"""
    count = 0
    for i in range(len(correct)):
        checkmark = ord(correct[i])-65
        locking = ord(lock[i])-65
        if checkmark != locking:
            rotate_down = down(checkmark, locking)
            rotate_up = upp(checkmark, locking)
            if rotate_up <= rotate_down:
                count += rotate_up
            elif rotate_down < rotate_up:
                count += rotate_down
    print(count)
safe(input().upper(), input().upper())
