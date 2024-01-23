#!/usr/bin/python3
"""Square with validations"""


class Square:
    """
    This is a class that defines a square.
    """
    def __init__(self, size=0):
        """
        This is the constructor method that initializes the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
