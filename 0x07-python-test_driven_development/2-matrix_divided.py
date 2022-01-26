"""

This module contains the function which can devide elements

"""


def matrix_divided(matrix, div):
    """
    division
    """
    a = 0
    b = 0
    lis = []
    for i in range(0, 2):
        for j in matrix[i]:
            if type(j) != float and type(j) != int:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
            if matrix[i] == 0:
                a += 1
            if matrix[i] == 1:
                b += 1
    if a != b:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for n in range(0, 2):
        lis.append(list(map(lambda x: round(x / 3, 2), matrix[n])))
    return lis
