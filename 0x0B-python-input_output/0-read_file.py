#!/usr/bin/python3
""" this module reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """
    this module   reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as f:
        contents = f.read()
        print(contents)
