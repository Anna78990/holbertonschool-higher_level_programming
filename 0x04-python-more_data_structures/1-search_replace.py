#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = []
    for i, x in enumerate(my_list):
        if x == search:
            tmp.append(replace)
        else:
            tmp.append(x)
    return tmp
