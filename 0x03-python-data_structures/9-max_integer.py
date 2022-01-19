#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mx = my_list[0]
        le = len(my_list)
        for i in range(1, le):
            if i == 0:
                continue
            elif mx < my_list[i]:
                mx = my_list[i]
            else:
                continue
        return mx
    else:
        return None
