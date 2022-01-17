#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    counter = 0

    for i in range(0, x):
        try:
            s += my_list[i]
            counter += 1
            print("{}".format(my_list[i]), end="")
        except TypeError:
            i += 1
    print()
    return counter
