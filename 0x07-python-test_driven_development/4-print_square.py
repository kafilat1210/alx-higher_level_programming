#!/usr/bin/python3
"""
This module provides a function to print a square of a given size.

The function checks the validity of the input parameter before printing.
"""


def print_square(size):
    """
    Prints a square of a given size.

    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer, or if it's a float and is less than 0
    ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
