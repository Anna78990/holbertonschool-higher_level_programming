#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        ap = a
        for i in range(1, b):
            ap *= a
        return ap
    else:
        an = a
        bn = abs(b)
        for i in range(1, bn):
            an *= a
        return 1 / an
