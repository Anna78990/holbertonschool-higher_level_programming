#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = []
        if len(matrix) > 0:
            for i in range(0, len(matrix)):
                new.append([])
                for j in range(0, len(matrix[i])):
                    a = matrix[i][j]
                    new[i].append(a * a)
            return new
        else:
            return matrix
    else:
        return matrix
