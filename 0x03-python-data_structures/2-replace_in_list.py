#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    le = len(my_list)
    if le < idx or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
