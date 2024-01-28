#!/usr/bin/python3

def matrix_divided(matrix, div):
    matrix2 = []

    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (matrix is None):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    j = len(matrix[0])
    for mylist in matrix:
        if (j != len(mylist)):
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(0, len(matrix)):
        divlist = []
        for x in range(0, len(matrix[i])):
            if (not isinstance(matrix[i][x], int) and not isinstance(matrix[i][x], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            number = matrix[i][x] / div
            dcmalstr = str(number)
            for r in range(0, len(dcmalstr)):
                if (dcmalstr[r] == "."):
                    decimals = len(dcmalstr) - r
                    number = "{:.2f}".format(number) if decimals > 2 else number
                    break;
            divlist.append(number)
        matrix2.append(divlist)
    return(matrix2)
