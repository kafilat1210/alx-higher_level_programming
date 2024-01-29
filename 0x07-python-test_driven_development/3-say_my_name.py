#!/usr/bin/python3
"""
This module contains a function that prints a person's full name.

The function accepts two parameters: first_name and last_name.
It validates the input parameters and then prints the full name in the format:
"My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's full name.

    Args:
    first_name (str): The person's first name.
    last_name (str): The person's last name. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the full name
    print("My name is {} {}".format(first_name, last_name))
