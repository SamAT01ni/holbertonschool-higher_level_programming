#!/usr/bin/python3
"""
"Divide Matrix" module
Divides elements in a matrix by a number
Returns new matrix of division results
"""


def matrix_divided(matrix, div):
    """Returns matrix of divided numbers.
    rounded to 2 decimal points.
    TypeError or ZeroDivisionError raised when thigns dont work
    """

    if (not isinstance(matrix, list) or
        len(matrix) == 0 or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for
                row in matrix for num in row)):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    rowlen = len(matrix[0])
    if not all(len(row) == rowlen for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), i)))
    return new_matrix
