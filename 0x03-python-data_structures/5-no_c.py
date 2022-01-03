#!/usr/bin/python3
def no_c(my_string):
    rp = list(my_string)
    le = len(rp) - 1
    for i in range(0, le):
        if rp[i] == 'c' or 'C':
            del rp[i]
    Rp = "".join(rp)
    return Rp
