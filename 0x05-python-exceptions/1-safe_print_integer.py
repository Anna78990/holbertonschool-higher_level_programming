#!/usr/bin/python3
def safe_print_integer(value):
    a = 0
    try:
        a += value
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
    except ValueError:
        return False
