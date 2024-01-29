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
        """"attribute getter method for width"""

        if not isinstance(value, int):
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
        """"attribute getter method for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area"""

        return self.width * self.height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """method to print the rectangular character"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        """ return the rectangle character"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
