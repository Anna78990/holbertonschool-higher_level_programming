#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        r = Rectangle(1, 2)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(0, 2)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(-1, 2)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(1, 2, 3, 4, 5)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
