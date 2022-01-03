#!/usr/bin/python3
def no_c(my_string):
    rp = list(my_string)
    le = len(rp) - 1
    for i in rp:
        if i == 'c' or 'C':
            del rp[i]
            del i
    Rp = "".join(rp)
    return Rp
