#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    if le <= idx or idx < 0:
        return None
    else:
        return my_list[idx]
