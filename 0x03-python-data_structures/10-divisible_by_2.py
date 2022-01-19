#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        boo = []
        le = len(my_list)
        for i in range(0, le):
            if my_list[i] % 2 == 0:
                boo.append(True)
            else:
                boo.append(False)
        return boo
    else:
        return None
