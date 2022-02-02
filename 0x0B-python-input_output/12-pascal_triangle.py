#!/usr/bin/python3
"""
this module contains function pascal_triangle
"""


def pascal_triangle(n):
    """
    function to make pascal_triangle
    """
    pl = []
    for i in range(0, n):
        if i == 0:
            pl.append([1])
        elif i == 1:
            pl.append([1, 1])
        else:
            m = []
            for num in range(0, i + 1):
                if num == 0:
                    m.append(1)
                elif num == i:
                    m.append(1)
                else:
                    a = i - 1
                    b = num - 1
                    s = pl[a][b] + pl[a][num]
                    m.append(s)
            pl.append(m)
    return pl
