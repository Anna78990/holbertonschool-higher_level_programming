#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    Ta = []
    Tb = []
    La = list(tuple_a)
    Lb = list(tuple_b)
    
    for i in range(0, 2):
        if La[i]:
            Ta.append(La[i])
        else:
            Ta.append(0)
    for j in range(0, 2):
        if Lb[j]:
            Tb.append(Lb[j])
        else:
            Tb.append(0)
    f = Ta[0] + Tb[0]
    s = Ta[1] + Tb[1]
    result.append(f)
    result.append(s)
    res = tuple(result)
    return res
