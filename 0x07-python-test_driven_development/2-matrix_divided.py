#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a num

The function checks the validity of the input parameters before dividing.
Each element of the resulting matrix is rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
    matrix (list): A list of lists of integers or floats.
    div (int or float): The number to divide each element of the matrix by.

    Returns:
    a new matrix with all elements in `matrix` divided by `div` error otherwise

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, if each
    row of the matrix does not have the same size, or if div is not a number.
    ZeroDivisionError: If div is zero.
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list:
        raise TypeError(err1)

    for elem in matrix:
        if type(elem) != list:
            raise TypeError(err1)

    row_size = len(matrix[0])
    for elem in matrix:
        if len(elem) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for items in elem:
            if type(items) not in (int, float):
                raise TypeError(err1)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    ret_matrix = []
    for elem in matrix:
        temp_list = []
        for items in elem:
            temp_list.append(round(items / div, 2))
        ret_matrix.append(temp_list)

    return ret_matrix
