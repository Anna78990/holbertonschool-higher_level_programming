#!/usr/bin/python3
"""

this module prints a text with 2 new lines after each of these
characters: ., ? and :

"""


def text_indentation(text):
    """
    prints 2 new lines after each of characters: ".", "?", ":"
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        a = i - 1
        if text[i] == " " and (text[a] == "." or text[a] == "?"
           or text[a] == ":" or text[a] == " "):
            continue
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
