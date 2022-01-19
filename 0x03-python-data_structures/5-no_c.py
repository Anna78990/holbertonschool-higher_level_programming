#!/usr/bin/python3
def no_c(my_string):
    stri = []
    if my_string:
        for i, x in enumerate(my_string):
            if x == 'c' or x == 'C':
                continue
            stri.append(x)
        st = "".join(stri)
        return st
    else:
        return my_string
