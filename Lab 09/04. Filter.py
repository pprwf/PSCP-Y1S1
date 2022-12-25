'''filter'''

import json

def main():
    """filter"""
    val = input()
    jso = ['0']
    tester = float(input())
    val = json.loads(val)
    for i in val:
        if val[i] >= tester:
            jso.append('%s %.2f' %(i, float(val[i])))
        else:
            pass
    if len(jso) >= 2:
        jso.remove('0')
    jso.sort()
    for i in jso:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
