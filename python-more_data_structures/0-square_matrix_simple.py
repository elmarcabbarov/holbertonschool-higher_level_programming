#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix_i = []
        for x in i:
            x = x ** 2
            new_matrix_i.append(x)
        new_matrix.append(new_matrix_i)
    return new_matrix
