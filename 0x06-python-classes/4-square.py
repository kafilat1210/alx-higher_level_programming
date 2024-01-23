#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """A class that defines a private
        instance attribute 'size'
    """

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.__size = size

    @property
    def size(self):
        """attribute getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """attribute setter method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """"Returns the area of square"""
        return self.__size ** 2
