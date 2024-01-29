#!/usr/bin/python3

"""Define a class called Rectangle"""


class Rectangle:
    """A class that defines 2 private instance
        attribute 'width' and  'height'
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                rectangle += str(self.print_symbol)
            if x < self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """__repr__ magic method"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """__del__ magic method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = Rectangle.area(rect_1)
        area2 = Rectangle.area(rect_2)

        if area1 >= area2:
            return rect_1
        return rect_2
