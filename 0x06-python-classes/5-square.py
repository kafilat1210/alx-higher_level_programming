#!/usr/bin/python3
"""Class of squares"""


class Square:
    """
    This is a class that defines a square.
    """
    def __init__(self, size=0):
        """
        This is the constructor method that initializes the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a method to get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a method to set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This is a method that calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This is a method that prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
