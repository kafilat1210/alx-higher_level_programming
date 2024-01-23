#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """A class that defines a private
        instance attribute 'size'
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) != int) or (type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """"attribute getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """attribute setter method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """"attribute getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """attribute setter method"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with
             the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """"method to print class"""

        result = ""
        if self.__size == 0:
            result = ""
        else:
            for j in range(self.__position[1]):
                result += "\n"
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    result += " "
                for k in range(self.__size):
                    result += "#"
                if i < self.__size - 1:
                    result += "\n"
        return result
