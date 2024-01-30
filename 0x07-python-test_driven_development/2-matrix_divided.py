#!/usr/bin/python3

"""
matrix divided module
"""


def matrix_divided(matrix, div):
    """
    matrix divided class
    """
    matrix2 = []
    Typeerr = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (matrix is None):
        raise TypeError(Typeerr)
    if (len(matrix) == 0):
        raise TypeError(Typeerr)
    j = len(matrix[0])
    for mylist in matrix:
        if (j != len(mylist)):
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(0, len(matrix)):
        divlist = []
        for x in range(0, len(matrix[i])):
            sym = matrix[i][x]
            if (not isinstance(sym, int) and not isinstance(sym, float)):
                raise TypeError(Typeerr)
            num = sym / div
            dcmalstr = str(num)
            for r in range(0, len(dcmalstr)):
                if (dcmalstr[r] == "."):
                    decimals = len(dcmalstr) - r
                    num = "{:.2f}".format(num) if decimals > 2 else num
                    break
            divlist.append(num)
        matrix2.append(divlist)
    return (matrix2)
