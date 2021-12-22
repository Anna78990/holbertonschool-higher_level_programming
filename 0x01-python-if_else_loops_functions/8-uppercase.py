#!/usr/bin/python3
def uppercase(str):
    i = 0
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            element = element.upper()
        print("{}".format(element), end="")
    print("")
