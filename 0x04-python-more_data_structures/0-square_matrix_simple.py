#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(0, len(matrix)):
        new.append([])
        for j in range(0, len(matrix)):
            a = matrix[i][j]
            new[i].append(a * a)
    return new
