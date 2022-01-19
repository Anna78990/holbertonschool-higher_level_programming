#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    Ta = []
    Tb = []
    if tuple_a:
        if len(tuple_a) < 2:
            Ta.append(tuple_a[0])
            Ta.append(0)
        else:
            for i in range(0, 2):
                Ta.append(tuple_a[i])
    else:
        for i in range(0, 2):
            Ta.append(0)
    if tuple_b:
        if len(tuple_b) < 2:
            Tb.append(tuple_b[0])
            Tb.append(0)
        else:
            for j in range(0, 2):
                Tb.append(tuple_b[j])
    else:
        for j in range(0, 2):
            Tb.append(0)
    f = Ta[0] + Tb[0]
    s = Ta[1] + Tb[1]
    result.append(f)
    result.append(s)
    res = tuple(result)
    return res
