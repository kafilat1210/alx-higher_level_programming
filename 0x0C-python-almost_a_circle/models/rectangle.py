#!/usr/bin/python3

"""Creates a class 'Rectangle' that inherits from 'Base'"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation with several private instance attributes

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
        """
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """"attribute getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """attribute setter method"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """"attribute getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """attribute setter method"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """"attribute getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """attribute setter method"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """"attribute getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """attribute setter method"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """"public method to return area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """"public method that prints in stdout the Rectangle"""
        for _ in range(self.__y):
            print("")
        for x in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for y in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Magic method for customised printing"""
        return "[Rectangle] " + \
               "({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y,
                                           self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to
            attribute using *args and **kwargs

           Args:
               *args (ints): no keyword argument
                  - 1st argument should be the id attribute
                  - 2nd argument should be the width attribute
                  - 3rd argument should be the height attribute
                  - 4th argument should be the x attribute
                  - 5th argument should be the y attribute

               **kwargs (dict): keyword arguments
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():

                    if key == "id":
                        self.id = value

                    elif key == "width":
                        self.width = value

                    elif key == "height":
                        self.height = value

                    elif key == "x":
                        self.x = value

                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Public method that returns the dictionary
            representation of a Rectangle
        """

        my_vars = {'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y}

        return my_vars
