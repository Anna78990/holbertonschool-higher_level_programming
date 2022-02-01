#!/usr/bin/python3
""" this module writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """
    this module writes a string to a text file (UTF8)
    filename(str): filename
    text(str): text written in file
    Return:number of characters written
    """
    with open(filename, 'w+') as f:
        contents = f.write(text)
        return contents
