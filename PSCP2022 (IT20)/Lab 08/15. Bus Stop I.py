'''bs1'''

def bus(passenger, stop, val=0):
    '''bus'''
    stop_num = []
    need = []
    for _ in range(stop):
        all_passenger = input().split()
        stop_num.append(all_passenger)
    stop_num.sort(key=lambda i: int(i[0]))
    for i in stop_num:
        bus_stop = int(i[0])
        if len(need) != 0:
            new_need = need.copy()
            for j in need:
                if j == bus_stop:
                    new_need.remove(j)
                    val += 1
            need = new_need
        for k in range(1, len(i)):
            if len(need) == passenger:
                break
            if bus_stop < int(i[k]):
                need.append(int(i[k]))
    print(val)
bus(int(input()), int(input()))
