#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        stri = list(my_string)
    else:
        return None
    for i, x in enumerate(stri):
        if x == 'c' or x == 'C':
            stri.remove(x)
    st = "".join(stri)
    return st
