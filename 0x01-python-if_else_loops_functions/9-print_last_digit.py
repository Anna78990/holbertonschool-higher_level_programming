#!/usr/bin/python3
def print_last_digit(number):
    ab = abs(number)
    print("{}".format(ab % 10), end="")
    return ab % 10
