#!/usr/bin/python3
"""
0-add_integer module
This module provides one function add_integer(a, b)
    prototype: def add_integer(a, b=98):
    a and b must be integers or float
"""


def add_integer(a, b=98):
    """
    Adds two integers.


    Args:
        a (int, float): The first parameter.
        b (int, float, optional): The second parameter. Defaults to 98.

    Returns:
        int: The return value, a + b casted to int.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

        a = int(a)
        b = int(b)

    return int(a) + int(b)
