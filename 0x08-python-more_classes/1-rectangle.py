#!/usr/bin/python3
"""
This module represent a class of rectangle with values for width and height
"""


class Rectangle:
    """
        This is a class of rectangle with width and height
    """

    def __init__(self, width=0, height=0):
        """initialization of width and height"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    @property
    def width(self):
        """get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """width is assigned a certain measurement"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value for height and raise error if otherwise"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
