#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matirx=[]
    for i in matrix:
        new_matirx_i= []
        for x in i:
            x = x ** 2
            new_matirx_i.append(x) 
        new_matirx.append(new_matirx_i)
    return new_matirx
