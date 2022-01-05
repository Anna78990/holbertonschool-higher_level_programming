#!/usr/bin/python3
def uniq_add(my_list=[]):
    ad = 0
    for i in range(0, len(my_list)):
        if i < len(my_list) - 1:
            a = i + 1
            for j in range(a, len(my_list)):
                if my_list[i] == my_list[j]:
                    break
                elif j == len(my_list) - 1:
                    ad += my_list[i]
                else:
                    continue
        else:
            ad += my_list[i]
    return ad
