#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update()
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 1)
    print(r1)

    r1.update(89, 1, 2)
    print(r1)

    r1.update(89, 1, 2, 3)
    print(r1)

    r1.update(89, 1, 2, 3)
    print(r1)

    r1.update(**{ 'id': 89 })
    print(r1)

    r1.update(**{ 'id': 89, 'width': 1, 'height': 2 })
    print(r1)

    r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
    print(r1)

    r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
    print(r1)

