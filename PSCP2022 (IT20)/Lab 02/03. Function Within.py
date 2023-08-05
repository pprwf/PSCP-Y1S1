'''within'''
 
def func(vala, valb, valc, vald):
    '''hi'''
    print(fff(fff(vala)))
    print(ggg(fff(vala - valb)))
    print(hhh(fff(vala + valb), fff(vala + valc), ggg(fff(vald ** 2))))
    print(iii(hhh(fff(vala + valb), fff(vala - valc), ggg(fff(vald ** 2))),
              ggg(fff(vala - valb)), fff(fff(fff(fff(fff(valc))))), vald ** 8))
 
def fff(valx):
    '''f(x)'''
    return 2 * valx
 
def ggg(valx):
    '''g(x)'''
    return 3 * valx ** 4 - valx ** 3 + 2 * valx ** 2 + 10
 
def hhh(valx, valy, valz):
    '''h(x)'''
    return (valz + valx) ** 2 - valx * valy + valy ** 2
 
def iii(vala, valb, valc, vald):
    '''i(x)'''
    return (vala ** 2 + valb ** 2 - valc ** 2) / (vald ** 2 - 2 * vala * vald + 2 * vala)
func(float(input()), float(input()), float(input()), float(input()))
