#!/usr/bin/python3

"""Define a class called Rectangle"""


class Rectangle:
    """A class that defines 2 private instance
        attribute 'width' and  'height'
    """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height attribute"""
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
        """"attribute getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """attribute setter method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """"attribute getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """attribute setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Magic method to print the rectangle with the character "#"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for x in range(self.__height):
            for _ in range(self.__width):
                rectangle += "#"
            if x < self.__height - 1:
                rectangle += "\n"

        return rectangle
