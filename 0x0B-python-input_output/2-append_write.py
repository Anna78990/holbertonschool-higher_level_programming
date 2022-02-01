#!/usr/bin/python3
""" this module appends a string to a text file (UTF8) """


def append_write(filename="", text=""):
    """
    this module appends a string to a text file (UTF8)
    filename(str): filename
    text(str): text written in file
    Return:number of characters written
    """
    with open(filename, 'a') as f:
        contents = f.write(text)
        return contents
