#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if (matrix is None):
        return (None)
    if (len(matrix) == 0):
        return (matrix)
    squaretrix = []
    for i in range(0, len(matrix)):
        sequence = []
        for j in range(0, len(matrix[i])):
            sequence.append(matrix[i][j] ** 2)
        squaretrix.append(sequence)
    return (squaretrix)
