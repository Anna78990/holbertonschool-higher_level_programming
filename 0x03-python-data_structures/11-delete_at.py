#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        le = len(my_list)
        if idx > le or idx < 0:
            return my_list
        for i in range(0, le):
            if i == idx:
                del my_list[i]
        return my_list
    else:
        return None