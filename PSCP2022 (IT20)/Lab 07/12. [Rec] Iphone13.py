'''i13'''

def pro(ver, cap, price=42900):
    '''i pro'''
    ver1, ver2 = ver == "iPhone 13 Pro", ver == "iPhone 13 Pro Max"
    cap1, cap2, cap3, cap4 = cap == "128 GB",\
cap == "256 GB", cap == "512 GB", cap == "1 TB"
    if ver1 and cap1:
        print(price - 4000)
    elif (ver1 and cap2) and (ver2 and cap1):
        print(price)
    elif ver1 and cap3:
        print(price + 8000)
    elif ver1 and cap4:
        print(price + 16000)
    elif ver2 and cap2:
        print(price + 4000)
    elif ver2 and cap3:
        print(price + 12000)
    elif ver2 and cap4:
        print(price + 20000)
    else:
        print("Not Available")

def iphone(ver, cap, price=29900):
    '''apple'''
    ver1, ver2 = ver == "iPhone 13 mini", ver == "iPhone 13"
    cap1, cap2, cap3 = cap == "128 GB", cap == "256 GB", cap == "512 GB"
    if ver1 and cap1:
        print(price - 4000)
    elif (ver1 and cap2) or (ver2 and cap1):
        print(price)
    elif ver1 and cap3:
        print(price + 8000)
    elif ver2 and cap2:
        print(price + 4000)
    elif ver2 and cap3:
        print(price + 12000)
    else:
        pro(ver, cap)
iphone(input(), input())
