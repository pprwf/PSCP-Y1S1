'''solar system'''

def temperature(posit, temp):
    '''temp'''
    for i, j in enumerate(posit):
        if i > 2 and posit[i - 3] + posit[i - 2] + posit[i - 1] + j == "Sun ":
            temp += str(i) + " "
        elif j == " " and  posit[i-3] + posit[i-2] + posit[i-1] + j != "Sun ":
            temp += str(i) + " "
    return temp

def solar(posit):
    '''solar system'''
    temp, hot, cool, left_star, right_star = temperature(posit, ""), "", "", None, None
    buffer, n_star, previous, previous_star, sun_pos = "", 0, -1, "", 0
    for i in temp:
        if i == " ":
            n_star += 1
            current = posit[previous+1:int(buffer)]
            if left_star is None:
                left_star = current + " "
            if current == "Sun":
                hot += previous_star + " "
                sun_pos = n_star
            if previous_star == "Sun":
                hot += current
            previous, previous_star = int(buffer), current
            buffer = ""
        elif i.isnumeric():
            buffer += str(i)
    if right_star is None:
        right_star = previous_star
    if posit.strip() != "Sun":
        if abs(1 - sun_pos) > abs(n_star - sun_pos):
            cool = left_star
        elif abs(1 - sun_pos) == abs(n_star - sun_pos):
            cool = left_star + right_star
        else:
            cool = right_star
    print("Hot: %s\nCool: %s"% (hot.strip(), cool.strip()))
solar(input()+' ')
