'''palindrome'''

def palindrome(next_num, time, add=0):
    '''palindrome'''
    while add != next_num:
        x_time = "%02d" % (int(time[-2:]) + 1)
        hour = time[0:2].replace(":", "")
        if int(x_time) % 60 == 0 and int(x_time) != 0:
            x_time = "00"
            y_time = int(hour) + 1
            hour = str(y_time)
        if int(hour) % 24 == 0:
            hour = "0"
        time = hour + ":" + x_time
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            add = add + 1
            print(time)
palindrome(int(input()), input())
