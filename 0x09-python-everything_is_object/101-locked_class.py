#!/usr/bin/python3
"""a class with a restricted object"""


class LockedClass:
    """class that prevents the user from dynamically
        creating new instance attributes"""
    def __setattr__(self, name, value):
        """Special method that is called when an attempt
            is made to set an attribute on an object"""
        if name != "first_name":
            raise AttributeError("'LockedClass' object\
 has no attribute '{}'".format(name))
        super().__setattr__(name, value)

    __slots__ = ["first_name"]
