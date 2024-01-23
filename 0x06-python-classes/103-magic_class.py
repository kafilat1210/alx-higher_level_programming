#!/usr/bin/python3
"""Define a class called MagicClass"""
import math


class MagicClass:
    """Python class MagicClass
        that does exactly the same
        as the given Python bytecode
    """
    def __init__(self, radius=0):
        """Instantiation with instance var radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of shape"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Return the circumference of shape"""
        return 2 * math.pi * self.__radius
