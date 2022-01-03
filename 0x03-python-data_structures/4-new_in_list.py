#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    le = len(my_list)
    new_list = list(range(le))
    l = le - 1
    for i in range(0, le):
        new_list[i] = my_list[i]
    if le < idx or idx < 0:
        return my_list
    else:
        new_list[idx] = element
        return new_list
