#!/usr/bin/python3
"""Module prints multiplication matrix
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices

    Args:
        m_a (list): list 1 of lists of integers or floats
        m_b (list): list 2 of lists of integers or floats

    Returns:
        a new matrix which is the product of the argument
        i.e ```m_a • m_b```; otherwise return error
    """
    err1 = "{} must be a list"
    err2 = "{} must be a list of lists"
    err3 = "{} can't be empty"
    err4 = "{} should contain only integers or floats"
    err5 = "each row of {} must be of the same size"
    err6 = "m_a and m_b can't be multiplied"

    if type(m_a) != list:
        raise TypeError(err1.format("m_a"))

    if type(m_b) != list:
        raise TypeError(err1.format("m_b"))

    for elem in m_a:
        if type(elem) != list:
            raise TypeError(err2.format("m_a"))

    for elem in m_b:
        if type(elem) != list:
            raise TypeError(err2.format("m_b"))

    if m_a == [] or m_a == [[]]:
        raise ValueError(err3.format("m_a"))

    if m_b == [] or m_b == [[]]:
        raise ValueError(err3.format("m_b"))

    for elem in m_a:
        for items in elem:
            if type(items) not in (int, float):
                raise TypeError(err4.format("m_a"))

    for elem in m_b:
        for items in elem:
            if type(items) not in (int, float):
                raise TypeError(err4.format("m_b"))

    row_size = len(m_a[0])
    for elem in m_a:
        if len(elem) != row_size:
            raise TypeError(err5.format("m_a"))

    row_size = len(m_b[0])
    for elem in m_b:
        if len(elem) != row_size:
            raise TypeError(err5.format("m_b"))

    no_cols_ma = len(m_a[0])
    no_rows_mb = len(m_b)

    if no_cols_ma != no_rows_mb:
        raise ValueError(err6)

    ret_matrix = []
    temp_list = []
    temp = 0
    rowX = 0

    for rowA in range(len(m_a)):
        for colB in range(len(m_b[0])):
            for colA in range(no_cols_ma):
                temp += (m_a[rowA][colA] * m_b[colA][colB])

            temp_list.append(temp)
            temp = 0

        ret_matrix.append(temp_list)
        temp_list = []

    return ret_matrix
