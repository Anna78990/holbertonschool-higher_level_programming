#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list) - 1
    if le > -1 and my_list != None:
        for i in range(le, -1, -1):
            print("{:d}".format(my_list[i]))
