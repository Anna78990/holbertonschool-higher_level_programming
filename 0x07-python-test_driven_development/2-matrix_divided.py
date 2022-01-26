#!/usr/bin/python3
"""

This module contains the function which can devide elements

"""


def matrix_divided(matrix, div):
    """
    division
    """
    lis = []
    if len(matrix) == 1:
        lis.append(list(map(lambda x: round(x / div, 2), matrix[0])))
        return lis
    for i in range(0, 2):
        for j in matrix[i]:
            if type(j) != float and type(j) != int:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for n in range(0, 2):
        lis.append(list(map(lambda x: round(x / div, 2), matrix[n])))
    return lis
