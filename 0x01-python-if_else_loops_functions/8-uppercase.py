#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            oe = ord(element) - 32
            element = chr(oe)
        print("{}".format(element), end="")
    print("")
