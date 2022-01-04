#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    columns = len(matrix)
    row = len(matrix[0])
    for i in range(columns):
        for j in range(row):
            if j < row and j > 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][j]), end="")
        print('')
