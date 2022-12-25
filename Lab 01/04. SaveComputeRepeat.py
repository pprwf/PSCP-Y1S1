'''save'''

def i_need_copy():
    '''ทำไมต้องเป็นรูปภาพ ขอเป็นตัวอักษรได้มั้ย มันก้อปไม่ได้อะ'''
    start = 492137954293754252786
    milliseconds = start
    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    print(days, hours, minutes, seconds, milliseconds)
i_need_copy()
