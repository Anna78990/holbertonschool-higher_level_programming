#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    if x == 0:
        return counter
    try:
        raise IndexError
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            counter += 1
    except IndexError:
        for i in my_list:
            print("{}".format(i), end="")
            counter += 1
    print("")
    return counter
