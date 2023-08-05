'''temp'''
 
def temp(fah):
    '''fahrenheit'''
    fah = (fah - 32) * 5 / 9
    print('%.1f Celsius' %fah)
temp(float(input()))
