'''ping'''

def failorsuccess(sent, success, fail, minimum, maximum):
    '''f/s'''
    if "Reply from" in sent:
        success += 1
        if "time=" in sent:
            if minimum >= int(sent[sent.find("time=") + 5:sent.find("ms")]):
                minimum = int(sent[sent.find("time=") + 5:sent.find("ms")])
            if maximum <= int(sent[sent.find("time=") + 5:sent.find("ms")]):
                maximum = int(sent[sent.find("time=") + 5:sent.find("ms")])
    else:
        fail += 1
    return success, fail, minimum, maximum

def average(sent, total):
    '''total'''
    if "Reply from" in sent and "time=" in sent:
        total += int(sent[sent.find("time=") + 5:sent.find("ms")])
    return total

def ping(success=0, fail=0, total=0):
    '''ping'''
    input()
    input()
    ip_address = input()
    if not "[" in ip_address:
        ip_address = ip_address[ip_address.find(" ") + 1:ip_address.find(" with")]
    else:
        ip_address = ip_address[ip_address.find("[") + 1:ip_address.find("]")]
    sent1, sent2, sent3, sent4 = input(), input(), input(), input()
    if "time=" in sent1:
        minimum, maximum = int(sent1[sent1.find("time=") + 5:sent1.find("ms")]),\
            int(sent1[sent1.find("time=") + 5:sent1.find("ms")])
    elif "time=" in sent2:
        minimum, maximum = int(sent2[sent2.find("time=") + 5:sent2.find("ms")]),\
            int(sent2[sent2.find("time=") + 5:sent2.find("ms")])
    elif "time=" in sent3:
        minimum, maximum = int(sent3[sent3.find("time=") + 5:sent3.find("ms")]),\
            int(sent3[sent3.find("time=") + 5:sent3.find("ms")])
    elif "time=" in sent4:
        minimum, maximum = int(sent4[sent4.find("time=") + 5:sent4.find("ms")]),\
            int(sent4[sent4.find("time=") + 5:sent4.find("ms")])
    else:
        minimum, maximum = 0, 0
    success, fail, minimum, maximum = failorsuccess(sent1, success, fail, minimum, maximum)
    success, fail, minimum, maximum = failorsuccess(sent2, success, fail, minimum, maximum)
    success, fail, minimum, maximum = failorsuccess(sent3, success, fail, minimum, maximum)
    success, fail, minimum, maximum = failorsuccess(sent4, success, fail, minimum, maximum)
    print("Ping statistics for %s:" %ip_address)
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss)," \
        %(success, fail, str(fail * 100 // 4) + "%"))
    if fail == 4:
        return
    print("Approximate round trip times in milli-seconds:")
    total = average(sent1, total)
    total = average(sent2, total)
    total = average(sent3, total)
    total = average(sent4, total)
    print("    Minimum = %dms, Maximum = %dms, Average = %dms" \
        %(minimum, maximum, total // success))
ping()
