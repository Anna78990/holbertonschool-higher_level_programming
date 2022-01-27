#!/usr/bin/python3

def text_indentation(text):
    if type(text) != str:
        TypeError("text must be a string")
    for i in range(0, len(text)):
        a = i - 1
        if text[i] == " " and (text[a] == "." or text[a] == "?" or\
            text[a] == ":"):
            continue
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
